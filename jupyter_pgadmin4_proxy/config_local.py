#via https://linuxhint.com/install-pgadmin4-ubuntu/
import os

# config settings, etc are stored in DATA_DIR. Should persist between
# sessions, so we put it under $HOME
DATA_DIR = os.path.realpath(os.path.expanduser('~/.pgadmin/'))

SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions.db')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')

# Wonder if server_mode is just for multiuser auth
SERVER_MODE = True
DEFAULT_SERVER = '0.0.0.0'
#DEFAULT_SERVER_PORT = 5050

DEBUG = True

import logging
FILE_LOG_LEVEL = logging.DEBUG
