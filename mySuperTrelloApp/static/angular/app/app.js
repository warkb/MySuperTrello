var Trello = angular.module('Trello', ["ngRoute"]);

Trello.config(['$routeProvider', function ($routeProvider){
    $routeProvider.when('/index', {
        templateUrl: 'static/angular/app/html/_main.html',
        controller: 'IndexController'
    });
}]);

Trello.controller('IndexController', ['$http', '$scope', function IndexController($http, $scope) {
    var self = this;
    $http.get('/get_descs').then(function (response) {
        console.log(response.data);
        $scope.descs = response.data;
    });
}]);