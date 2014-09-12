from flask import Blueprint, render_template

mod = Blueprint("general", __name__)

@mod.route("/")
def index():
    return render_template("general/index.html", name="Igor")

@mod.route("/films")
def film_list():
    return render_template("general/film_list.html")

@mod.route("/films/<string:film_page>")
def film(film_page):
    f = {'title': 'hello', 'director': 'Tkachev Igor', 'story': 'asdfasdfasdfasdasdfasdfasdfasdfas asdfasdfas'}
    return render_template("general/film.html", film=f)