angular.module("app",[]);

angular.module("app").controller("vm", function($scope, $element) {
    vm = $scope;

    //APPEND for DEMO purposes
    vm.html = '<script>alert("Hello John!");</script><p>Loaded</p>';
    $element.append(vm.html);

    //FIND script and eval
    var js = $element.find("script")[0].innerHTML;
    eval(js);

