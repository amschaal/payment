angular.module("payment", ["payment.tpls","payment.directives"]);
angular.module("payment.tpls", ["template/payment/archive.html"]);

angular.module('payment.directives', ['models'])//,'angular-growl'
.directive('archivePayment', function(Payment) {
	  return {
	    restrict: 'AE',
	    templateUrl: 'template/payment/archive.html',
	    scope: {
	    	payment:'='
	    },
	    controller: function($scope, $http, $element){
	    	this.$scope = $scope;
	    	$scope.archive = function (){
// 	    		$scope.payment.archived = true;
	    		$scope.payment.$archive(function(){
// 	    			growl.success('Payment "'+$scope.payment.id+'" archived',{ttl: 4000});
	    		},function(){
// 	    			$scope.payment.archived=false;
// 	    			growl.error('Error archiving payment "'+$scope.payment.id+'"',{ttl: 4000});
	    		});
	    	}
	    	$scope.unarchive = function (){
// 	    		$scope.payment.archived = false;
	    		$scope.payment.$unarchive(function(){
// 	    			growl.success('Payment "'+$scope.payment.id+'" unarchived',{ttl: 4000});
	    		},function(){
// 	    			$scope.payment.archived=true;
// 	    			growl.error('Error unarchiving payment "'+$scope.payment.id+'"',{ttl: 4000});
	    		});
	    	}
	    }
	  }
	});


angular.module('template/payment/archive.html', []).run(['$templateCache', function($templateCache) {
	  $templateCache.put('template/payment/archive.html',
	'<span ng-if="payment.status==\'UNPAID\'"><button ng-click="archive()" ng-if="payment && !payment.archived" class="btn btn-default btn-sm btn-success"><i class="fa fa-folder-open-o" aria-hidden="true"></i> Archive</button><button ng-click="unarchive()" ng-if="payment && payment.archived" class="btn btn-default btn-sm btn-warning"><i class="fa fa-folder-o" aria-hidden="true"></i> Unarchive</button></span>'
	  );
	}]);

