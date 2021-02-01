import sys
import os
import site

HERE = os.path.dirname(os.path.abspath(__file__))

def setup_pgadmin4():
    '''Manage a pgadmin4 instance.'''

    name = 'pgadmin4'
    def _get_pgadmin4_cmd(port):
        site_packages_path = site.getsitepackages()[0]
        current_config_path = os.path.join(HERE, 'config_local.py')
        target_config_path = os.path.join(site_packages_path, 'pgadmin4', 'config_local.py')

        # FIXME: Overrides any existing config_local user may have. This is in our local
        # venv install, so it's ok.
        if os.path.exists(target_config_path):
            os.remove(target_config_path)
        os.symlink(current_config_path, target_config_path)
        return [
            'gunicorn',
            '-b',
            '127.0.0.1:{port}',
            '-e',
            'SCRIPT_NAME={base_url}pgadmin4',
            '--chdir',
            os.path.join(site_packages_path, 'pgadmin4'),
            'pgAdmin4:app',
        ]

    return {
        'command': _get_pgadmin4_cmd,
        'absolute_url': True,
        'timeout': 120,
        'launcher_entry': {
            'title': 'pgadmin4',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'shiny.svg')
        }
    }
