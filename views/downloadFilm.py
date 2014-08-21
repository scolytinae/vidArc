from flask import Blueprint
from flask import request
from flask import render_template

mod = Blueprint("downloadFilm", __name__)

@mod.route("/download")
def downloadFilm():
    if request.method == "GET":
        return render_template("download_film/index.html")