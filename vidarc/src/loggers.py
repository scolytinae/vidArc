from logging.handlers import RotatingFileHandler
import logging


def add_loggers(app):
    app.logger.setLevel(logging.INFO)
    add_file_logger(app, logging.INFO)
    add_mail_logger(app, logging.ERROR)


def add_file_logger(app, log_level=logging.INFO):
    file_name = app.config['LOG_FILE_NAME']
    if file_name != '':
        file_handler = RotatingFileHandler(file_name, 'a', app.config['LOG_FILE_SIZE'], app.config['LOG_FILES_COUNT'])
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(log_level)
        app.logger.addHandler(file_handler)
        app.logger.info('start app')


def add_mail_logger(app, log_level=logging.INFO):
    pass