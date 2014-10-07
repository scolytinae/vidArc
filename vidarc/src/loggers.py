from os import path
from logging.handlers import RotatingFileHandler
import logging

DEFAULT_FILE_SIZE = 1 * 1024 * 1024
DEFAULT_FILES_COUNT = 10
DEFAULT_TMP_DIR = '.'
LOG_FILE_NAME = 'vidarc.log'


def add_loggers(app):
    app.logger.setLevel(logging.INFO)
    add_file_logger(app, logging.INFO)
    add_mail_logger(app, logging.ERROR)


def add_file_logger(app, log_level=logging.INFO):
    tmp_dir = DEFAULT_TMP_DIR
    if 'TMP_DIR' in app.config:
        tmp_dir = app.config['TMP_DIR']

    file_size = DEFAULT_FILE_SIZE
    if 'LOG_FILE_SIZE' in app.config:
        file_size = app.config['LOG_FILE_SIZE']

    files_count = DEFAULT_FILES_COUNT
    if 'LOG_FILES_COUNT' in app.config:
        files_count = app.config['LOG_FILES_COUNT']

    file_handler = RotatingFileHandler(path.join(tmp_dir, LOG_FILE_NAME), 'a', file_size, files_count)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(log_level)
    app.logger.addHandler(file_handler)


def add_mail_logger(app, log_level=logging.INFO):
    pass