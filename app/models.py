from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(160))
    email = db.Column(db.String(120), index=True, unique=True)
    last_seen = db.Column(db.DateTime)
    recipes = db.relationship('Recipe', backref='', lazy='dynamic')
    meals = db.relationship('Meal', backref='', lazy='dynamic')
    menus = db.relationship('Menu', backref='', lazy='dynamic')


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    comments = db.Column(db.Text)


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(160))
    description = db.Column(db.Text)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(160))
    directions = db.Column(db.Text)
    ingredients = db.Column(db.Text)
