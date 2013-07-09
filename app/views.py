from flask import jsonify, abort, make_response, request, url_for
from flask.ext.httpauth import HTTPBasicAuth
from app import app, db
from models import User, Menu, Meal, Recipe


auth = HTTPBasicAuth()


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/mealplan/api/v1.0/menu', methods=['GET'])
#@auth.login_required
def get_menus():
    return jsonify({'menus': 'menus'})


@app.route('/mealplan/api/v1.0/menu/<int:menu_id>', methods=['GET'])
#@auth.login_required
def get_menu(menu_id):
    menu = Menu.query.get(int(menu_id))
    if len(menu) == 0:
        abort(404)
    return jsonify({'menu': menu})


@app.route('/mealplan/api/v1.0/menu', methods=['POST'])
#@auth.login_required
def create_menu():
    if not request.json or not 'start_date' in request.json:
        abort(404)
    menu = {}
    db.session.add(menu)
    db.session.commit()
    return jsonify({'menu': menu}), 201


@app.route('/mealplan/api/v1.0/menu/<int:menu_id>', methods=['PUT'])
#@auth.login_required
def update_menu(menu_id):
    return jsonify({'menu': 'menu'})


@app.route('/mealplan/api/v1.0/menu/<int:menu_id>', methods=['DELETE'])
#@auth.login_required
def delete_menu(menu_id):
    menu = Menu.query.get(int(menu_id))
    if len(menu) == 0:
        abort(404)
    db.session.delete(menu)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/mealplan/api/v1.0/meal', methods=['GET'])
#@auth.login_required
def get_meals():
    return jsonify({'meals': 'meals'})


@app.route('/mealplan/api/v1.0/meal/<int:meal_id>', methods=['GET'])
#@auth.login_required
def get_meal(meal_id):
    meal = Meal.query.get(int(meal_id))
    if len(meal) == 0:
        abort(404)
    return jsonify({'meal': meal[0]})


@app.route('/mealplan/api/v1.0/meal', methods=['POST'])
#@auth.login_required
def create_meal():
    if not request.json or not 'start_date' in request.json:
        abort(404)
    meal = {}
    db.session.add(meal)
    db.session.commit()
    return jsonify({'meal': meal}), 201


@app.route('/mealplan/api/v1.0/meal/<int:meal_id>', methods=['PUT'])
#@auth.login_required
def update_meal(meal_id):
    return jsonify({'meal': 'meal'})


@app.route('/mealplan/api/v1.0/meal/<int:meal_id>', methods=['DELETE'])
#@auth.login_required
def delete_meal(meal_id):
    meal = Meal.query.get(int(meal_id))
    if len(meal) == 0:
        abort(404)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/mealplan/api/v1.0/recipe', methods=['GET'])
#@auth.login_required
def get_recipes():
    return jsonify({'recipes': 'recipes'})


@app.route('/mealplan/api/v1.0/recipe/<int:recipe_id>', methods=['GET'])
#@auth.login_required
def get_recipe(recipe_id):
    recipe = Recipe.query.get(int(recipe_id))
    if len(recipe) == 0:
        abort(404)
    return jsonify({'recipe': recipe[0]})


@app.route('/mealplan/api/v1.0/recipe', methods=['POST'])
#@auth.login_required
def create_recipe():
    if not request.json or not 'start_date' in request.json:
        abort(404)
    recipe = {}
    db.session.add(recipe)
    db.session.commit()
    return jsonify({'recipe': recipe}), 201


@app.route('/mealplan/api/v1.0/recipe/<int:recipe_id>', methods=['PUT'])
#@auth.login_required
def update_recipe(recipe_id):
    return jsonify({'recipe': 'recipe'})


@app.route('/mealplan/api/v1.0/recipe/<int:recipe_id>', methods=['DELETE'])
#@auth.login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(int(recipe_id))
    if len(recipe) == 0:
        abort(404)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unathorized access'}), 403)
