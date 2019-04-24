var Trello = angular.module('Trello', ["ngRoute"]);

Trello.config(['$routeProvider', function ($routeProvider){
    $routeProvider.when('/index', {
        templateUrl: 'static/angular/app/html/_main.html',
        controller: 'IndexController'
    });
}]);

Trello.controller('IndexController', function IndexController($scope) {
    var descsJson = JSON.parse($('#descsJson').attr('value'));
    console.log(descsJson);
    $scope.descs = descsJson;
});