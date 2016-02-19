var app = angular.module('app', [])

app.controller('AppCtrl', function($http){
  var this_ = this;
  this_.message = 'Test';
});