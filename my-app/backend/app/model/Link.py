from .BaseModel import BaseModel, db
from sqlalchemy.orm import relationship


class Link(BaseModel, db.Model):
    __tablename__ = "link"
    original_url = db.Column(db.String, nullable=False)
    hash_url = db.Column(db.String, nullable=False)
    expired = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('user.id'))

    def __init__(self, original_url, hash_url, expired, user_id):
        self.original_url = original_url
        self.hash_url = hash_url
        self.expired = expired
        self.user_id = user_id
        super().__init__()
