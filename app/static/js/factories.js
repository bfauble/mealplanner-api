angular.module('mealPlanner.factories', [])
	.factory('Recipe', function($resource) {
		return $resource('/mealplan/api/v1.0/recipe/:id', { id: '@recipe.name' });
	})
	.factory('Meal', function($resource){
		return $resource('/mealplan/api/v1.0/meal/:id', { id: '@meal.id' });
	})
	.factory('Menu', function($resource){
		return $resource('/mealplan/api/v1.0/menu/:id', { id: '@menu.id' });
	});