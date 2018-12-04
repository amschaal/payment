var transformDjangoRestResponse = function(data, headers){
	try {
        var jsonObject = JSON.parse(data); // verify that json is valid
        return jsonObject.results;
    }
    catch (e) {
        console.log("did not receive a valid Json: " + e)
    }
    return {};
}

var standard_methods = {
	    query: { method: 'GET', transformResponse:transformDjangoRestResponse, isArray:true },
	    save : { method : 'PUT' },
	    patch : { method : 'PATCH' },
	    create : { method : 'POST' },
	    remove : { method : 'DELETE' }
	  };

angular.module('models', ['ngResource'])
.factory('Payment', ['$resource', function ($resource) {
  return $resource('/api/payments/:id/', {id:'@id'}, standard_methods);
}]);
