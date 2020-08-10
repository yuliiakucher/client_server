from db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def json(self):
        return {'name': self.name, 'email': self.email}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
