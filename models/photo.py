from vidArc import db
from general import BaseItem, types


class Film(BaseItem):
    id = db.Column(db.Integer, db.ForeignKey('base_item.id'), primary_key=True)


    __tablename__ = 'film'

    __mapper_args__ = {
        'polymorphic_identity': types.PHOTO_ALBUM
    }
