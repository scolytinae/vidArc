#--* coding: utf-8 *--
from flask import Blueprint, render_template

mod = Blueprint("general", __name__)

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi."

FILMS = [
    {'title': u'Первый мститель: Другая война', 'director': 'Tkachev Igor', 'story': LOREM_IPSUM, 'href': 'films/1'},
    {'title': 'hello2', 'director': 'Tkachev Igor', 'story': 'hello world'}
]


@mod.route("/")
def index():
    return render_template("general/index.html", items=FILMS)


@mod.route("/films")
def film_list():
    return render_template("general/film_list.html", films=FILMS)


@mod.route("/films/<string:film_page>")
def film(film_page):
    return render_template("general/film.html", film=FILMS[0])