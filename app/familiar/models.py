import enum

from .. import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    familiarity_level = db.Column(db.String(70), nullable=False)
    familiar = db.relationship('Familiar', backref='category', lazy=True)


class Gender(enum.Enum):
    male = 'male'
    female = 'female'


class Familiar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(70), nullable=False)
    first_name = db.Column(db.String(70), nullable=False)
    phone_number = db.Column(db.String(70), nullable=False)
    gender = db.Column(db.Enum(Gender))
    birth_date = db.Column(db.String(70), nullable=True)
    hobby = db.Column(db.String(70), nullable=True)
    category_familiar_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Familiar('{self.id}', '{self.last_name}')"