(function() {
'use strict;'

angular.module('app', ['ngAnimate', ])
  .config(['$resourceProvider', function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false
    }])
  .config(['$interpolateProvider',
    function($interpolateProvider) {
      $interpolateProvider.startSymbol('[[').endSymbol(']]')
    }])
  .config(['$httpProvider',
    function($httpProvider) {
      $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
    }])
  .config(['$httpProvider',
    function($httpProvider) {
      var getCookie;
      getCookie = function(name) {
        var cookie, _i, _len, _ref
        _ref = document.cookie.split(';')
        for (_i = 0, _len = _ref.length; _i < _len; _i++) {
          cookie = _ref[_i]
          if (cookie && name === (cookie.trim().split('='))[0]) {
            return decodeURIComponent(cookie.trim().slice(1 + name.length))
          }
        }
        return null
      }
    return $httpProvider.defaults.headers.common['X-CSRFToken'] = getCookie("csrftoken")
  }])

  .directive('fileModel', ['$parse', function ($parse) {
    return {
      restrict: 'A',
      link: function(scope, element, attrs) {
        var model = $parse(attrs.fileModel)
        var modelSetter = model.assign        
        element.bind('change', function(){
          scope.$apply(function(){
            modelSetter(scope, element[0].files[0])
          })
        })
      }
    }
  }])

angular.module('app.services', ['ngResource', ])
  .factory('Obj', ['$resource',
    function($resource){
      return $resource('objects/:pk/')
    }])

/*
var newObj = new Obj()
newObj.name = ""
newObj.description = ""
newObj.$save()

Obj.get({pk:1})
  .$promise.then(function(obj){
    $scope.obj = obj
  })
*/

angular.module('app.controllers', [])
  .controller('ObjCtrl', [ '$scope',
    function ObjCtrl($scope){
      Obj.query(function(response){
        $scope.objs = response
      })
    $scope.submit = function(name, description) {
      var newObj = new Obj()
        newObj.name = name
        newObj.description = description
      newObj.$save(function(){
        $scope.objs.unshift(newObj)
      })
    }

    }])


})();
