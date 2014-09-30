from vidArc import db

TYPE_FILM = 1
TYPE_AUDIO_ALBUM = 2
TYPE_AUDIO = 3
TYPE_PHOTO_ALBUM = 4
TYPE_PHOTO = 5


class DownloadedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    type = db.Column(db.SmallInteger, default=TYPE_FILM)

    def __init__(self, title, type):
        self.title = title
        self.type = type

    def __repr__(self):
        return '<Item {0}>' % (self.title)