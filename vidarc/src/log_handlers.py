from os import path

DEFAULT_FILE_SIZE = 1 * 1024 * 1024
DEFAULT_FILES_COUNT = 10


def create_file_handler(tmp_dir, file_size=DEFAULT_FILE_SIZE):
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(path.join(tmp_dir, 'vidarc.log'), 'a', file_size, DEFAULT_FILES_COUNT)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    return file_handler


def create_mail_handler(app):
    pass