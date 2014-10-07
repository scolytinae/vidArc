from __init__ import db
from vidarc.models.general import BaseItem, types


class AudioAlbum(BaseItem):
    id = db.Column(db.Integer, db.ForeignKey('base_item.id'), primary_key=True)
    year = db.Column(db.Date)
    author = db.Column(db.String(64))
    track_count = db.Column(db.Integer)
    tracks = db.relationship('Audio', backref='album', lazy='dynamic')

    __tablename__ = 'audio_album'

    __mapper_args__ = {
        'polymorphic_identity': types.AUDIO_ALBUM
    }


class Audio(BaseItem):
    id = db.Column(db.Integer, db.ForeignKey('base_item.id'), primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('audio_album.id'))

    __tablename__ = 'audio'

    __mapper_args__ = {
        'polymorphic_identity': types.AUDIO
    }
