from flask import Flask
from flask import render_template
from flask import g

from views import general, downloadFilm
import sqlite3

app = Flask(__name__)
app.config.from_object("siteconfig")


def connect_db():
    rw = sqlite3.connect(app.config["DATABASE"])
    rw.row_factory = sqlite3.Row
    return rw


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    if not hasattr(g, "_database"):
        g._database = connect_db()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    if hasattr(g, "_database"):
        g._database.close()


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

app.register_blueprint(general.mod)
app.register_blueprint(downloadFilm.mod)