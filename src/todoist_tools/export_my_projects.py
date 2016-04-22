import json
import os
import sys
import argparse
import configparser
from datetime import datetime
from collections import OrderedDict
import todoist

from utils import urlify, get_jinja2_template, login_to_todoist


config = configparser.ConfigParser()
config.read('config.ini')


def get_projects(api):
    """ Return all projects informations as an OrderedDict.
        Projects are populated with a key 'project_items' with their items informations.

        api is a todoist.TodoistAPI instance where you are logged in !

        Deleted or archived projects and items are ignored.
    """
    response = api.sync(resource_types=['all'])

    # Compute projects as an OrderedDict - keys are projects ids

    projects = []
    for project in response['Projects']:
        if project['is_deleted'] == 0 and project['is_archived'] == 0:
            project['project_items'] = []
            projects.append(project)

    projects_dict = OrderedDict()
    for project in sorted(projects, key=lambda p: p['item_order']):
        projects_dict[project['id']] = project

    # Add items to projects (list)

    for item in response['Items']:
        if item['is_deleted'] == 0 and item['is_archived'] == 0 and item['in_history'] == 0:
            projects_dict[item['project_id']]['project_items'].append(item)

    # Sort items in projects
    for project in projects_dict.values():
        project['project_items'] = sorted(project['project_items'], key=lambda i: i['item_order'])

    return projects_dict


def export_to_txt(projects, filepath='todoist.txt', indent='    '):
    """ Save projects and items in a TEXT file.

        projects is an OrderedDict containing project information (see get_projects)
    """
    lines = []

    for project in projects.values():
        project_indent = (project['indent'] - 1) * indent
        if project['indent'] == 1:
            lines.append('\n')
        lines.append('{}* {}\n'.format(project_indent, project['name']))

        for item in project['project_items']:
            item_indent = project_indent + item['indent'] * indent
            lines.append('{}- {} (due_date_utc={} ; date_string={} ; priority={})\n'.format(
                item_indent,
                item['content'],
                item['due_date_utc'] or '',
                item['date_string'],
                item['priority'],
            ))

    with open(filepath, 'w') as f:
        f.writelines(lines)


def export_to_json(projects, filepath='todoist.json'):
    """ Save projects and items in a JSON file.

        projects is an OrderedDict containing project information (see get_projects)
    """
    with open(filepath, 'w') as f:
        f.write(json.dumps(projects, sort_keys=True, indent=4))


def export_to_html(projects, filepath='todoist.html'):
    """ Save projects and items in a HTML file.

        projects is an OrderedDict containing project information (see get_projects)
    """

    template = get_jinja2_template('export_my_projects.html')

    main_projects_menu = []
    projects_data = []

    for project_id, project in projects.items():

        # main menu
        if project['indent'] == 1:
            main_projects_menu.append({
                'id': project_id,
                'name': project['name']
            })

        # project and items
        data = {
            'id': project_id,
            'name': project['name'],
            'margin_left': (project['indent'] - 1) * 30,  # in pixel
            'project_items': [],
            'num_items': len(project['project_items'])
        }
        for item in project['project_items']:
            data['project_items'].append({
                'content': urlify(item['content']),
                'due_date_utc': item['due_date_utc'] or '',
                'date_string': item['date_string'],
                'priority': item['priority'],
                'margin_left': (item['indent'] - 1) * 30,  # in pixel
            })

        projects_data.append(data)

    with open(filepath, 'w') as f:
        f.write(template.render(
            main_projects_menu=main_projects_menu,
            projects=projects_data
        ))


if __name__ == '__main__':

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--dirpath',
        help='Target directory path',
        type=str,
        default='.'
    )
    parser.add_argument(
        '-f', '--format',
        help='Outpup format',
        type=str,
        choices=['txt', 'json', 'html'],
        default='html'
    )
    args = parser.parse_args()

    # Compute file path
    file_name = '{}-todoist.{}'.format(
        datetime.now().strftime('%Y-%m-%d'),
        args.format
    )
    target_path = os.sep.join([args.dirpath, file_name])

    # Generate export
    todoist_api = todoist.TodoistAPI()

    if login_to_todoist(todoist_api, config['todoist']['email'], config['todoist']['password']):
        all_projects = get_projects(todoist_api)
        if args.format == 'txt':
            export_to_txt(all_projects, filepath=target_path)
        elif args.format == 'json':
            export_to_json(all_projects, filepath=target_path)
        else:
            export_to_html(all_projects, filepath=target_path)
        sys.stdout.write('Export saved to {}\n'.format(target_path))
    else:
        sys.stderr.write('An error occured.\n')
