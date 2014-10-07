from flask import Blueprint
from flask import render_template
from flask import flash
from vidarc.forms.download import DownloadForm

mod = Blueprint("download", __name__)


@mod.route('/download', methods=['GET', 'POST'])
def download():
    form = DownloadForm()
    if form.validate_on_submit():
        #try to download file in form.address
        pass
    return render_template("download/index.html", form=form)
