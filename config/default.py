import os

_basedir = os.path.abspath(os.path.dirname(__file__) + '/../')

DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')

LOG_FILE_SIZE = 10 * 1024 * 1024
LOG_FILES_COUNT = 10

TORRENT_PORTS = (6881, 6891)

TMP_DIR = os.path.join(_basedir, 'tmp/')
LOG_FILE_NAME = os.path.join(TMP_DIR, 'vidarc.log')
LOG_MAIL_SERVER = ''

CSRF_ENABLED = True

del os
