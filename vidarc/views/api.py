from flask import Blueprint
from flask import jsonify
from flask import request

DOWNLOADS = [
    {
        'id': 1,
        'title': 'hello1',
        'done': False
    },
    {
        'id': 2,
        'title': 'hello2',
        'done': False
    }
]

mod = Blueprint("api", __name__)

@mod.route('/api/downloads-long', methods=['GET'])
@mod.route('/api/downloads', methods=['GET', 'POST', 'DELETE'])
def get_downloads():
    if request.method == 'POST':
        add_download_item()
    elif request.method == 'DELETE':
        delete_download_item()
    else:
        return jsonify({'downloads': DOWNLOADS})


def delete_download_item():
    pass


def add_download_item():
    pass