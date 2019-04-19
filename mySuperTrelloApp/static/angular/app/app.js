var app = angular.module('Trello', [
    'ui.router',
    'restangular'
])

app.config(function ($stateProvider, $urlRouterProvider, RestangularProvider) {
    // For any unmatched url, send to /route1
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('index', {

            url: "/",
            templateUrl: "html/_main.html",
            controller: "Mainpage"
        })
})

app.controller("Mainpage", ['$scope', 'Restangular', 'CbgenRestangular', '$q',
function ($scope, Restangular, CbgenRestangular, $q) {


}])// end controller