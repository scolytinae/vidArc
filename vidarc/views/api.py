from flask import Blueprint
from flask import jsonify
from flask import request

import time

DOWNLOADS = [
    {
        'id': 1,
        'title': 'hello1',
        'done': False,
        'cmd': 'add'
    },
    {
        'id': 2,
        'title': 'hello2',
        'done': False,
        'cmd': 'add'
    }
]

mod = Blueprint("api", __name__)

@mod.route('/api/downloads', methods=['GET', 'POST', 'DELETE'])
def get_downloads():
    if request.method == 'GET':
        if request.args.get('type', '') == 'full':
            return jsonify({'data': get_downloads()})

        return jsonify({'data': wait_downloads()})

    if request.method == 'POST':
        add_download_item()

    if request.method == 'DELETE':
        delete_download_item()


def get_downloads():
    return DOWNLOADS


def wait_downloads():
    return []


def update_downloads():
    pass


def delete_download_item():
    pass


def add_download_item():
    pass