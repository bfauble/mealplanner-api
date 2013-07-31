angular.module('mealPlanner.controllers', [])
	.controller('Mealplan', function($scope) {
		
	})
	.controller('EditRecipe', function($scope, $routeParams, $resource, Recipe) {
		var recipes = Recipe.get({id:$routeParams.index}, function() {
			console.log(recipes.message.recipe);
			$scope.recipe = recipes.message.recipe[0];
		});
	})
	.controller('AddRecipe', function($scope, $routeParams) {
		
	})
	.controller('DeleteRecipe', function($scope, $routeParams, $location) {

	})
	.controller('ListRecipes', function($scope, $routeParams, $resource, Recipe) {
		var recipes = Recipe.get({}, function() {
			console.log(recipes.message.recipe);
			$scope.recipes = recipes.message.recipe;
		});
	})
	.controller('EditMeal', function($scope, $routeParams, $resource, Meal) {
		var meals = Meal.get({id:$routeParams.index}, function() {
			console.log(meals.message.meal);
			$scope.meal = meals.message.meal[0];
		});
	})
	.controller('AddMeal', function($scope, $routeParams) {

	})
	.controller('DeleteMeal', function($scope, $routeParams, $location) {

	})
	.controller('ListMeals', function($scope, $routeParams, $resource, Meal) {
		var meals = Meal.get({}, function() {
			console.log(meals.message.meal);
			$scope.meals = meals.message.meal;
		});
	})
	.controller('EditMenu', function($scope, $routeParams, $resource, Menu) {
		var menus = Menu.get({id:$routeParams.index}, function() {
			console.log(menus.message.menu);
			$scope.menu = menus.message.menu[0];
		});
	})
	.controller('AddMenu', function($scope, $routeParams) {

	})
	.controller('DeleteMenu', function($scope, $routeParams, $location) {

	})
	.controller('ListMenus', function($scope, $routeParams, $resource, Menu) {
		var menus = Menu.get({}, function() {
			console.log(menus.message.menu);
			$scope.menus = menus.message.menu;
		});
	});
