from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

from views import general, downloadFilm

app = Flask(__name__)
app.config.from_object("siteconfig")

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

app.register_blueprint(general.mod)
app.register_blueprint(downloadFilm.mod)