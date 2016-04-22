import os
import sys
import re
import jinja2


_link = re.compile(r'(?:(http://)|(https://)|(www\.))(\S+\b/?)([!"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]*)(\s|$)', re.I)


def urlify(text):
    """ Convert TEXT links to HTML """

    def links_text2html(match):
        groups = match.groups()
        protocol_http = groups[0] or ''  # may be None
        protocol_https = groups[1] or ''  # may be None
        www_lead = groups[2] or ''  # may be None
        if protocol_http:
            return '<a href="http://{1}{2}" target="_blank">{0}{1}{2}</a>{3}{4}'.format(protocol_http, www_lead,
                                                                                        *groups[3:])
        elif protocol_https:
            return '<a href="http://{1}{2}" target="_blank">{0}{1}{2}</a>{3}{4}'.format(protocol_https, www_lead,
                                                                                        *groups[3:])
        else:
            # www
            return '<a href="http://{1}{2}" target="_blank">{0}{1}{2}</a>{3}{4}'.format(protocol_http, www_lead,
                                                                                        *groups[3:])

    return _link.sub(links_text2html, text)


def get_jinja2_template(template_name):
    """ Return a jinja2 template from the "templates" directory """
    try:
        module_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    except NameError:
        # __file__ not available
        module_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    templates_path = os.sep.join([module_path, 'templates'])
    templates_env = jinja2.Environment(loader=jinja2.FileSystemLoader([templates_path]))
    return templates_env.get_template(template_name)


def login_to_todoist(api, username, password):
    """ Login to Todoist, return True if ok else False

        api is a todoist.TodoistAPI instance
    """
    user = api.login(username, password)
    if 'error' in user:
        sys.stderr.writelines('{} ({}): {}\n'.format(
            user['error_tag'], user['error_code'], user['error']
        ))
        return False
    return True
