var mealPlanner = angular
	.module('mealPlanner', ['mealPlanner.controllers', 'mealPlanner.directives', 'mealPlanner.factories', 'ngResource'])
	.config(function($routeProvider) {
		$routeProvider
			.when ('/', {
			})
			.when('/recipe/', {
				templateUrl: "/static/recipe/list.html",
				controller: 'ListRecipes'
			})
			.when('/meal/', {
				templateUrl: "/static/meal/list.html",
				controller: 'ListMeals'
			})
			.when('/menu/', {
				templateUrl: "/static/menu/list.html",
				controller: 'ListMenus'
			})
			.when('/recipe/:index', {
				templateUrl: "/static/recipe/edit.html",
				controller: 'EditRecipe'
			})
			.when('/meal/:index', {
				templateUrl: "/static/meal/edit.html",
				controller: 'EditMeal'
			})
			.when('/menu/:index', {
				templateUrl: "/static/menu/edit.html",
				controller: 'EditMenu'
			})
			.when('/recipe/add', {
				templateUrl: "/static/recipe/edit.html",
				controller: 'AddRecipe'
			})
			.when('/meal/add', {
				templateUrl: "/static/meal/edit.html",
				controller: 'AddMeal'
			})
			.when('/menu/add', {
				templateUrl: "/static/menu/edit.html",
				controller: 'AddMenu'
			})
			.when('/recipe/delete/:index', {
				templateUrl: "/static/recipe/edit.html",
				controller: 'DeleteRecipe'
			})
			.when('/meal/delete/:index', {
				templateUrl: "/static/meal/edit.html",
				controller: 'DeleteMeal'
			})
			.when('/menu/delete/:index', {
				templateUrl: "/static/menu/edit.html",
				controller: 'DeleteMenu'
			});
	});
