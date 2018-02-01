angular.module('myApp',['ngRoute'])
    .controller('AppCtrl', function($scope) {



    })
    .controller('MenuCtrl', function($scope,$rootScope) {
    $scope.groups = [{'name':'服务器管理','module':'serserm','childs':[{'name':'添加服务器','module':'adds'},{'name':'查询服务','module':'selects'}]},{'name':'操作平台','module':'action','childs':[{'name':'服务器操作','module':'saction'},{'name':'区组操作','module':'sidaction'}]}];
    /* $scope.index='管理平台' */
    $rootScope.pageview = {'添加服务器':'添加服务器',
        '查询服务':'查询服务',
        '服务器操作':'选择服务器操作',
        '区组操作':'选择区组操作'
    }
    $rootScope.index='管理平台';
    $rootScope.value=$rootScope.index;
    $scope.select = function(parentname,pagename) {
        $rootScope.value=$rootScope.index + ' / ' + parentname + ' / ' +  pagename;
        $rootScope.second_name =  $rootScope.pageview[pagename];
    }

})
    .controller('SlistCtrl', function($scope,$rootScope) {
        /*
         $rootScope.qudao = {
         苹果渠道: {name:'app'},
         混服渠道: {name:'360'},
         请选择渠道:{name:'请选择子渠道'},

         }
         */

        $rootScope.qudao = {
            苹果渠道: ['app', '小米'],
            混服渠道: ['360', '华为'],
            请选择渠道: ['请选择子渠道'],
        }
    })
    .controller('SServerGroup', function($scope,$rootScope) {
        $rootScope.servergroup = [
            {'name':'测试渠道','opgameid':1001},
            {'name':'苹果渠道','opgameid':2001},
            {'name':'混服渠道','opgameid':3001},

        ]
        $scope.servers = [
            {'opgameid':1001,'lan_ip':'192.168.1.1','serverStatus':4},
            {'opgameid':1001,'lan_ip':'192.168.1.2','serverStatus':4},
            {'opgameid':2001,'lan_ip':'192.168.2.1','serverStatus':4},
            {'opgameid':2001,'lan_ip':'192.168.2.2','serverStatus':4},
            {'opgameid':3001,'lan_ip':'192.168.3.1','serverStatus':4},
            {'opgameid':3001,'lan_ip':'192.168.3.2','serverStatus':4},
        ]


    })
    .config(['$routeProvider', function($routeProvider){
        $routeProvider
            .when('/',{template:''})
            .when('/adds',{templateUrl: 'views/adds.html'})
            .when('/selects',{templateUrl: 'views/selects.html'})
            .when('/action',{template:''})
            .when('/saction',{templateUrl: 'views/saction.html'})
            .when('/sidaction',{templateUrl: 'views/sidaction.html'})

            .otherwise({redirectTo:'/'});
    }]);
