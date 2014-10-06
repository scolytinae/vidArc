from vidArc import db

types = {
    'NONE': 0,
    'FILM': 1,
    'AUDIO_ALBUM': 2,
    'AUDIO': 3,
    'PHOTO_ALBUM': 4
}


class BaseItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    href = db.Column(db.String(128))
    type = db.Column(db.SmallInteger)

    __tablename__ = 'base_item'

    __mapper_args__ = {
        'polymorphic_identity': types.NONE,
        'polymorphic_on': type
    }

    def __init__(self, title, type):
        self.title = title
        self.type = type

    def __repr__(self):
        return '<Item {0}>' % (self.title)
