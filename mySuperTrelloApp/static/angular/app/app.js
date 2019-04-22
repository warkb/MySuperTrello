var Trello = angular.module('Trello', ["ngRoute"]);

Trello.config(['$routeProvider', function ($routeProvider){
    $routeProvider.when('/index', {
        templateUrl: 'static/angular/app/html/_main.html',
        controller: 'IndexController'
    });
}]);

Trello.controller('IndexController', function IndexController($scope) {
    console.log('IndexController');
});