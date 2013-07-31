angular.module('mealPlanner.directives', [])
	.directive('recipeEditor', function() {
		return {
			restrict: 'E',
			transclude: true,
			replace: true,
			compile: function(tElement, tAttrs, transclude) {
				scope.editRecipe = function() {

				};

				return function(scope, element, attrs) {

				}
			}
		}
	})
	.directive('mealEditor', function() {
		return {
			restrict: 'E',
			transclude: true,
			replace: true,
			compile: function(tElement, tAttrs, transclude) {
				scope.editMeal = function() {

				};

				return function(scope, element, attrs) {

				}
			}
		}
	})
	.directive('menuEditor', function() {
		return {
			restrict: 'E',
			transclude: true,
			replace: true,
			compile: function(tElement, tAttrs, transclude) {
				scope.editMenu = function() {

				};

				return function(scope, element, attrs) {

				}
			}
		}
	});