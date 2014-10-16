from flask import Blueprint
from flask import jsonify

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


@mod.route('/api/downloads', methods=['GET'])
def get_downloads():
    return jsonify({'downloads': DOWNLOADS})

