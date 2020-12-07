import hashlib
from .BaseModel import BaseModel, db
from sqlalchemy.orm import relationship


class User(BaseModel, db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    links = db.relationship('Link', backref='user', cascade='delete')

    def __init__(self, username, password):
        self.username = username
        self.password = User.set_password(password)
        super().__init__()

    @staticmethod
    def set_password(pw):
        secure = hashlib.md5()
        secure.update(pw.encode("utf-8"))
        secure_password = secure.hexdigest()
        return secure_password
