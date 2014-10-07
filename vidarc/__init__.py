from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

from src.torrent_server import TorrentServer
from src.loggers import add_loggers
from views import general, download

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
app.config.from_envvar('VIDARC_SETTINGS', silent=True)

add_loggers(app)

db = SQLAlchemy(app)
torrent_server = TorrentServer(app, db)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

app.register_blueprint(general.mod)
app.register_blueprint(download.mod)