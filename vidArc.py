from flask import Flask
from flask import render_template
from flask import g

from views import general

app = Flask(__name__)
app.config.from_object("siteconfig")

def connect_db():
    rw = sqlite3.connect(app.config["DATABASE"])
    rw.row_factory = sqlite3.Row
    return rw

def init_db():
    db = get_db()
    with app.open_resource("schema.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
	db = g._database = connect_db()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
	db.close();

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

app.register_blueprint(general.mod)