from __init__ import db


class TorrentFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(256))
    torrent_path = db.Column(db.String(256))