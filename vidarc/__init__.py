from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

import src.log_handlers as lh

from src.torrent_server import TorrentServer
from views import general, downloadFilm

app = Flask(__name__)
app.config.from_object("siteconfig")

if not app.debug:
    import logging
    app.logger.setLevel(logging.INFO)

    file_size = lh.DEFAULT_FILE_SIZE
    if 'LOG_FILE_SIZE' in app.config:
        file_size = app.config['LOG_FILE_SIZE']
    file_handler = lh.create_file_handler(app.config['TMP_DIR'], file_size)
    app.logger.addHandler(file_handler)
    app.logger.info('starting vidarc application...')

db = SQLAlchemy(app)
torrent_server = TorrentServer(app, db)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

app.register_blueprint(general.mod)
app.register_blueprint(downloadFilm.mod)