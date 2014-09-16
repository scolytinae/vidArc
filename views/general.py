#--* coding: utf-8 *--
from flask import Blueprint, render_template

mod = Blueprint("general", __name__)

LOREM_IPSUM = u"После беспрецедентных событий, впервые собравших вместе команду Мстителей, Стив Роджерс, известный также как Капитан Америка, оседает в Вашингтоне и пытается приспособиться к жизни в современном мире. Но покой этому герою только снится — пытаясь помочь коллеге из агентства Щ. И. Т, Стив оказывается в центре событий, грозящих катастрофой мирового масштаба. Для того, чтобы разоблачить злодейский заговор, Капитан Америка объединяется с Черной вдовой. К ним также присоединяется новый соратник, известный как Сокол, однако никто из них даже не подозревает, на что способен новый враг."

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