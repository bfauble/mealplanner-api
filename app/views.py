from flask import jsonify, abort, make_response, request, url_for, render_template, send_from_directory
from flask.ext.httpauth import HTTPBasicAuth
from app import app, db
from models import User, Menu, Meal, Recipe, MenuMeal


auth = HTTPBasicAuth()


@app.route('/')
def index():
    return make_response(open('app/static/index.html').read())
    #return render_template('index.html', angular=url_for('static', filename='js/testing.js'))


@app.route('/addmenu')
def add_menu():
    return render_template('addmenu.html', url=url_for('create_menu'))


@app.route('/addmeal')
def add_meal():
    return render_template('addmeal.html', url=url_for('create_meal'))


@app.route('/addrecipe')
def add_recipe():
    return render_template('addrecipe.html', url=url_for('create_recipe'))


@app.route('/mealplan/api/v1.0/menu', methods=['GET'])
#@auth.login_required
def get_menus():
    menu = db.session.query(Menu).all()
    if len(menu) == 0:
        abort(404)
    return jsonify(message={"menu": [i.serialize for i in menu]})


@app.route('/mealplan/api/v1.0/menu/<int:menu_id>', methods=['GET'])
#@auth.login_required
def get_menu(menu_id):
    menu = db.session.query(Menu).filter_by(id=str(menu_id)).all()
    if len(menu) == 0:
        abort(404)
    return jsonify(message={"menu": [i.serialize for i in menu]})


@app.route('/mealplan/api/v1.0/menu', methods=['POST'])
#@auth.login_required
def create_menu():
    if not request.json:
        abort(404)
    menu = Menu()
    db.session.add(menu)
    menu.load(request.json)
    db.session.commit()
    for meal in request.json['meals']:
        meal['menu_id'] = menu.id
        mm = MenuMeal()
        mm.load(meal)
        db.session.add(mm)
    db.session.commit()
    return jsonify({'menu': menu.serialize}), 201


@app.route('/mealplan/api/v1.0/menu/<int:menu_id>', methods=['PUT'])
#@auth.login_required
def update_menu(menu_id):
    menu = Menu.query.get(int(menu_id))
    if menu is None:
        abort(404)
    menu.load(request.json)
    db.session.add(menu)
    db.session.commit()
    return jsonify(message={'menu': True}), 200


@app.route('/mealplan/api/v1.0/menu/<int:menu_id>', methods=['DELETE'])
#@auth.login_required
def delete_menu(menu_id):
    menu = Menu.query.get(int(menu_id))
    if menu is None:
        abort(404)
    db.session.delete(menu)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/mealplan/api/v1.0/meal', methods=['GET'])
#@auth.login_required
def get_meals():
    meal = db.session.query(Meal).all()
    if len(meal) == 0:
        abort(404)
    return jsonify(message={"meals": [i.serialize for i in meal]})


@app.route('/mealplan/api/v1.0/meal/<int:meal_id>', methods=['GET'])
#@auth.login_required
def get_meal(meal_id):
    meal = db.session.query(Meal).filter_by(id=str(meal_id)).all()
    if len(meal) == 0:
        abort(404)
    return jsonify(message={"meal": [i.serialize for i in meal]})


@app.route('/mealplan/api/v1.0/meal', methods=['POST'])
#@auth.login_required
def create_meal():
    if not request.json:
        abort(404)
    meal = Meal()
    db.session.add(meal)
    meal.load(request.json)
    db.session.commit()
    return jsonify({'meal': meal.serialize}), 201


@app.route('/mealplan/api/v1.0/meal/<int:meal_id>', methods=['PUT'])
#@auth.login_required
def update_meal(meal_id):
    meal = Meal.query.get(int(meal_id))
    if meal is None:
        abort(404)
    meal.load(request.json)
    db.session.add(meal)
    db.session.commit()
    return jsonify(message={'meal': True}), 200


@app.route('/mealplan/api/v1.0/meal/<int:meal_id>', methods=['DELETE'])
#@auth.login_required
def delete_meal(meal_id):
    meal = Meal.query.get(int(meal_id))
    if meal is None:
        abort(404)
    db.session.delete(meal)
    db.session.commit()
    return jsonify({'result': True}), 202


@app.route('/mealplan/api/v1.0/recipe', methods=['GET'])
#@auth.login_required
def get_recipes():
    #Filter based on user
    recipe = db.session.query(Recipe).all()
    if len(recipe) == 0:
        abort(404)
    return jsonify(message={"recipe": [i.serialize for i in recipe]})


@app.route('/mealplan/api/v1.0/recipe/<int:recipe_id>', methods=['GET'])
#@auth.login_required
def get_recipe(recipe_id):
    recipe = db.session.query(Recipe).filter_by(id=str(recipe_id)).all()
    if len(recipe) == 0:
        abort(404)
    return jsonify(message={"recipe": [i.serialize for i in recipe]})


@app.route('/mealplan/api/v1.0/recipe', methods=['POST'])
#@auth.login_required
def create_recipe():
    if not request.json:
        abort(404)
    recipe = Recipe()
    db.session.add(recipe)
    recipe.load(request.json)
    db.session.commit()
    return jsonify(message={"recipe": recipe.serialize}), 201


@app.route('/mealplan/api/v1.0/recipe/<int:recipe_id>', methods=['PUT'])
#@auth.login_required
def update_recipe(recipe_id):
    recipe = Recipe.query.get(int(recipe_id))
    if recipe is None:
        abort(404)
    recipe.load(request.json)
    db.session.add(recipe)
    db.session.commit()
    return jsonify(message={'recipe': True}), 200


@app.route('/mealplan/api/v1.0/recipe/<int:recipe_id>', methods=['DELETE'])
#@auth.login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(int(recipe_id))
    if recipe is None:
        abort(404)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify(message={'result': True}), 202


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(message={'error': 'Not found'}), 404)


@auth.error_handler
def unauthorized():
    return make_response(jsonify(message={'error': 'Unathorized access'}), 403)
