from __init__ import db
from vidarc.models.general import BaseItem, types


class Film(BaseItem):
    id = db.Column(db.Integer, db.ForeignKey('base_item.id'), primary_key=True)
    director = db.Column(db.String(64))
    story = db.Column(db.Text)
    picture_href = db.Column(db.String(128))

    __tablename__ = 'film'

    __mapper_args__ = {
        'polymorphic_identity': types.FILM
    }