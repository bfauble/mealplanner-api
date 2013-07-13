from app import db
from datetime import datetime


meal_to_recipe_table = db.Table('meal_to_recipe', db.Model.metadata,
    db.Column('meal_id', db.Integer, db.ForeignKey('meal.id')),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(160), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    last_seen = db.Column(db.DateTime)
    recipes = db.relationship('Recipe', backref='author', lazy='dynamic')
    meals = db.relationship('Meal', backref='author', lazy='dynamic')
    menus = db.relationship('Menu', backref='author', lazy='dynamic')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'last_seen': self.last_seen
        }

    def __repr__(self):
        return "User(%r, %r, %r, %r, %r, %r, %r)" % (self.id, self.username, self.email, self.last_seen, self.recipes, self.meals, self.menus)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.Text)
    meals = db.relationship('MenuMeal')

    def load(self, params):
        self.author_id = params['author_id']
        self.start_date = datetime.strptime(params['start_date'], "%Y-%m-%d").date()
        self.end_date = datetime.strptime(params['end_date'], "%Y-%m-%d").date()
        self.comments = params['comments']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'author': self.author_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'comments': self.comments,
            'meals': self.serialize_m_to_m
        }

    @property
    def serialize_m_to_m(self):
        return [item.serialize for item in self.meals]

    def __repr__(self):
        return "Menu(%r, %r, %r, %r, %r, %r)" % (self.id, self.author_id, self.start_date, self.end_date, self.comments, self.meals)


class MenuMeal(db.Model):
    meal_date = db.Column('meal_date', db.DateTime, nullable=False)
    meal_time = db.Column('meal_time', db.String(10), nullable=False)
    menu_id = db.Column('menu_id', db.Integer, db.ForeignKey('menu.id'), primary_key=True)
    meal_id = db.Column('meal_id', db.Integer, db.ForeignKey('meal.id'), primary_key=True)
    meal = db.relationship('Meal')

    def load(self, params):
        self.meal_date = datetime.strptime(params['meal_date'], "%Y-%m-%d").date()
        self.meal_time = params['meal_time']
        self.menu_id = params['menu_id']
        self.meal_id = params['meal_id']

    @property
    def serialize(self):
        return {
            'meal_date': self.meal_date,
            'meal_time': self.meal_time,
            'meal_id': self.meal_id,
            'meal': self.serialize_m_to_m
        }

    @property
    def serialize_m_to_m(self):
        return self.meal.serialize

    def __repr__(self):
        return "MenuMeal(%r, %r, %r, %r)" % (self.meal_date, self.meal_time, self.menu_id, self.meal_id)


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(160), nullable=False)
    description = db.Column(db.Text)
    recipes = db.relationship('Recipe', secondary=meal_to_recipe_table)

    def load(self, params):
        self.author_id = params['author_id']
        self.title = params['title']
        self.description = params['description']
        for rec in params['recipes']:
            recipe = db.session.query(Recipe).filter_by(id=str(rec)).one()
            self.recipes.append(recipe)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'author': self.author_id,
            'title': self.title,
            'description': self.description,
            'recipes': self.serialize_m_to_m
        }

    @property
    def serialize_m_to_m(self):
        return [item.serialize for item in self.recipes]

    def __repr__(self):
        return "Meal(%r, %r, %r, %r, %r)" % (self.id, self.author_id, self.title, self.description, self.recipes)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(160), nullable=False)
    directions = db.Column(db.Text)
    ingredients = db.Column(db.Text)

    def load(self, params):
        self.author_id = params['author_id']
        self.title = params['title']
        self.directions = params['directions']
        self.ingredients = params['ingredients']

    @property
    def serialize(self):
        return {
            'id': self.id,
            'author': self.author_id,
            'title': self.title,
            'directions': self.directions,
            'ingredients': self.ingredients
        }

    def __repr__(self):
        return "Recipe(%r, %r, %r, %r, %r)" % (self.id, self.author_id, self.title, self.directions, self.ingredients)
