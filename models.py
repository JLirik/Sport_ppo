from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    email = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String, nullable=False)

    def get_id(self):
        return str(self.email)
