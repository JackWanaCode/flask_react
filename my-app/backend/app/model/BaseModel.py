from datetime import datetime
from api import app
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

# print("Asdfasdf", app.config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
# print("Asdfasdf", app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

# print("ASDfasdf", db)


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self):
        self.id = uuid4()
        self.date_created = datetime.utcnow()

    def add(self):
        self.updated_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def save(self):
        self.updated_at = datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)
