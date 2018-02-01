/**
 * Created by liushuo on 2017/8/2.
 */
var reserver = 'http://192.168.137.1:8000/'
var httpserver = 'http://192.168.137.1:90/'

function myrefresh() {
    window.location.reload();
}

/* csrf */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

header = {'X-CSRFToken': csrftoken }



/* user_serch_ad init */

$(function () {
    $("#tb_user").bootstrapTable({
        toolbar: "#toolbar",
        idField: "Id",
        pagination: true,
        showRefresh: true,
        search: true,
        clickToSelect: true,
        queryParams: function (param) {
            return {};
        },
        url: reserver + "api/search/User/",
        columns: [{
            checkbox: true
        },
            {
                field: "AccountID",
                title: "用户ID",
            }
            ,{
                field: "name",
                title: "用户名",
                editable: {
                    type: 'text',
                    title: '用户名',
                    validate: function (v) {
                        if (!v) return '用户名不能为空';

                    }
                }
            }, {
                field: "username",
                title: "昵称",
                editable: {
                    type: 'text',
                    title: '昵称',
                    validate: function (v) {
                        if (!v) return '昵称不能为空';

                    }
                }
            }, {
                field: "created_at",
                title: "生日",
                formatter : function (value, row, index) {
                    return moment(row.created_at).format("YYYY-MM-DD hh:mm:ss");
                },

            },],
        onEditableSave: function (field, row, oldValue, $el) {
            var id = row.AccountID
            $.ajax({
                type: "put",
                url: reserver + "api/v1/User/" + id + '/',
                data: row,
                dataType: 'JSON',
                xhrFields: {
                    withCredentials: true
                },
                crossDomain: true,
                headers: header,
                success: function (data, status) {
                    if (status == "success") {
                        alert('提交数据成功');
                        myrefresh()
                    }
                },
                error: function () {
                    alert('编辑失败');
                    myrefresh()
                },
                complete: function () {

                }

            });
        }
    });
});

/* 删除按钮 */
function ReqDuser(id) {
    $.ajax({
        cache: true,
        headers: header,
        type: "DELETE",
        url: reserver + 'api/v1/User/' + id + '/',
        async: false,
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            myrefresh()
            alert('删除成功')
        }
    });
}
function D_User() {

    var S_all = $("#tb_user").bootstrapTable('getAllSelections');
    for (i = 0;i < S_all.length; i++ )
    {
       /*  alert(S_all[i].AccountID) */
        ReqDuser(S_all[i].AccountID)
    }


}


/* 编辑按钮 */
function ReqEuser(id) {
    alert( $('#EUser_Lay').serialize())
    $.ajax({
        data: $('#EUser_Lay').serialize(),
        cache: true,
        type: "PUT",
        headers: {'X-CSRFToken': csrftoken },
        url: reserver + 'api/v1/User/' + id + '/',
        async: false,
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            alert('修改成功')
        }
    });
}
function E_User() {
    S_obj = $("#tb_user").bootstrapTable('getAllSelections')
    if ( S_obj.length == 1 ) {
        fields = ['AccountID','name','username','from_id','project_id']
        /* alert('getSelections: ' + JSON.stringify(S_obj)) */
        /* JsonId= JSON.stringify(S_obj) */
        var JsonData = S_obj[0]

        var Json_AccountID = JsonData.AccountID
        var Json_name = JsonData.name
        var Json_username = JsonData.username
        var Json_from_id = JsonData.from_id
        var Json_project_id = JsonData.project_id
    }
    else
    {
        alert('请勾选一个进行修改')
    }
    /* var html = '<form class="layui-form layui-form-pane" id="EUser_Lay"> <div class="layui-form-item"> <label class="layui-form-label">用户名</label> <div class="layui-input-inline"> <input type="text" name="name" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input" value=' + Json_name + '> </div> </div> <div class="layui-form-item"> <div class="layui-form-item"> <label class="layui-form-label">所属项目</label> <div class="layui-input-inline"> <input type="text" name="project" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input"> <!-- input type="text" name="title" autocomplete="off" placeholder="请输入项目" class="layui-input" --> </div> </div> <div class="layui-form-item"> <div class="layui-input-block"> <input type="button" onclick="ReqEuser(' + Json_AccountID + ')" class="layui-btn layui-btn-primary" value="提交"></input> <input type="reset" class="layui-btn layui-btn-primary"></input> </div> </div> </form>' */
    var html = '<div style="margin: 50px auto; width: 50%"><form class="layui-form layui-form-pane" id="EUser_Lay"> <div class="layui-form-item"> <label class="layui-form-label">用户名</label> <div class="layui-input-inline"> <input type="text" name="name" lay-verify="required" placeholder="请输入用户名" autocomplete="off" class="layui-input" value=' + Json_name + '> </div> </div> <div class="layui-form-item"><label class="layui-form-label">用户昵称</label> <div class="layui-input-inline"> <input type="text" name="username" lay-verify="required" placeholder="请输入昵称" autocomplete="off" class="layui-input" value=' + Json_username + '> </div> </div>  <div class="layui-form-item"> <div class="layui-form-item"> <label class="layui-form-label">所属项目</label> <div class="layui-input-inline"> <input type="text" name="project" lay-verify="required" placeholder="请输入项目" autocomplete="off" class="layui-input">  </div> </div> <div class="layui-form-item"> <div class="layui-input-block"> <input type="button" onclick="ReqEuser(' + Json_AccountID + ')" class="layui-btn layui-btn-primary" value="提交"></input> <input type="reset" class="layui-btn layui-btn-primary"></input> </div> </div> </form></div>'
    E_Layuser(html)
}
function E_Layuser(html){
    //示范一个公告层
    layer.open({
        type: 1
        ,title: false //不显示标题栏
        ,closeBtn: false
        ,area: '50%'
        ,shade: 0.8
        ,id: 'LAY_layuipro' //设定一个id，防止重复弹出
        ,btn: ['火速围观', '残忍拒绝']
        ,moveType: 1 //拖拽模式，0或者1
        /* ,content: '<div style="padding: 50px; line-height: 22px; background-color: #393D49; color: #fff; font-weight: 300;">你知道吗？亲！<br>layer ≠ layui<br><br>layer只是作为Layui的一个弹层模块，由于其用户基数较大，所以常常会有人以为layui是layerui<br><br>layer虽然已被 Layui 收编为内置的弹层模块，但仍然会作为一个独立组件全力维护、升级。<br><br>我们此后的征途是星辰大海 ^_^</div> */
        ,content:html
        ,success: function(layero){
            var btn = layero.find('.layui-layer-btn');
            btn.css('text-align', 'center');
            btn.find('.layui-layer-btn0').attr({
                href: 'http://www.layui.com/'
                ,target: '_blank'
            });
        }
    });
}



/* 显示登录名 */









/*初始化弹出框 */

layui.use('layer', function(){ //独立版的layer无需执行这一句
    var $ = layui.jquery, layer = layui.layer; //独立版的layer无需执行这一句


    //触发事件
    var active = {
        setTop: function(){
            var that = this;
            //多窗口模式，层叠置顶
            layer.open({
                type: 2 //此处以iframe举例
                ,title: '当你选择该窗体时，即会在最顶端'
                ,area: ['390px', '260px']
                ,shade: 0
                ,maxmin: true
                ,offset: [ //为了演示，随机坐标
                    Math.random()*($(window).height()-300)
                    ,Math.random()*($(window).width()-390)
                ]
                ,content: 'http://layer.layui.com/test/settop.html'
                ,btn: ['继续弹出', '全部关闭'] //只是为了演示
                ,yes: function(){
                    $(that).click();
                }
                ,btn2: function(){
                    layer.closeAll();
                }

                ,zIndex: layer.zIndex //重点1
                ,success: function(layero){
                    layer.setTop(layero); //重点2
                }
            });
        }

        ,C_User: function(){
            //示范一个公告层
            layer.open({
                type: 1
                ,title: false //不显示标题栏
                ,closeBtn: false
                ,area: '50%'
                ,shade: 0.8
                ,id: 'LAY_layuipro' //设定一个id，防止重复弹出
                ,btn: ['火速围观', '残忍拒绝']
                ,moveType: 1 //拖拽模式，0或者1
                /* ,content: '<div style="padding: 50px; line-height: 22px; background-color: #393D49; color: #fff; font-weight: 300;">你知道吗？亲！<br>layer ≠ layui<br><br>layer只是作为Layui的一个弹层模块，由于其用户基数较大，所以常常会有人以为layui是layerui<br><br>layer虽然已被 Layui 收编为内置的弹层模块，但仍然会作为一个独立组件全力维护、升级。<br><br>我们此后的征途是星辰大海 ^_^</div> */
                ,content:'<div style="margin: 50px auto; width: 50%"><form class="layui-form layui-form-pane" id="CUser_Lay"> <div class="layui-form-item" > <label class="layui-form-label">用户名</label> <div class="layui-input-inline"> <input type="text" name="name" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input"> <!-- input type="text" name="title" autocomplete="off" placeholder="请输入登录名" class="layui-input" --> </div> </div> <div class="layui-form-item"> <label class="layui-form-label">密码</label> <div class="layui-input-inline"> <input type="password" name="password1" placeholder="请输入密码" autocomplete="off" class="layui-input"> </div> <div class="layui-form-mid layui-word-aux">请务必填写用户名</div> </div> <div class="layui-form-item"> <label class="layui-form-label">确认密码</label> <div class="layui-input-inline"> <input type="password" name="password2" placeholder="请输入密码" autocomplete="off" class="layui-input"> </div> <div class="layui-form-mid layui-word-aux">请务必填写用户名</div> </div> <div class="layui-form-item"> <label class="layui-form-label">所属项目</label> <div class="layui-input-inline"> <input type="text" name="project" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input"> <!-- input type="text" name="title" autocomplete="off" placeholder="请输入登录名" class="layui-input" --> </div> </div> <div class="layui-form-item"> <div class="layui-input-block"> <input type="button" onclick="CUser_Lay()" class="layui-btn layui-btn-primary" value="提交"></input> <input type="reset" class="layui-btn layui-btn-primary"></input> </div> </div> </form></div>'
                ,success: function(layero){
                    var btn = layero.find('.layui-layer-btn');
                    btn.css('text-align', 'center');
                    btn.find('.layui-layer-btn0').attr({
                        href: 'http://www.layui.com/'
                        ,target: '_blank'
                    });
                }
            });
        }
        ,confirmTrans: function(){
                    //配置一个透明的询问框
                    layer.msg('你确认要进行删除吗', {
                        time: 20000, //20s后自动关闭
                        btn: ['知道了',"<span onclick='D_User()'>确认删除</span>"]});
        }
        ,offset: function(othis){
            var type = othis.data('type')
                ,text = othis.text();

            layer.open({
                type: 1
                ,offset: type //具体配置参考：http://www.layui.com/doc/modules/layer.html#offset
                ,id: 'LAY_demo'+type //防止重复弹出
                ,content: '<div style="padding: 20px 100px;">'+ text +'</div>'
                ,btn: '关闭全部'
                ,btnAlign: 'c' //按钮居中
                ,shade: 0 //不显示遮罩
                ,yes: function(){
                    layer.closeAll();
                }
            });
        }
    };

    $('.site-demo-button .layui-btn').on('click', function(){
        var othis = $(this), method = othis.data('method');
        active[method] ? active[method].call(this, othis) : '';
    });

});

/* 单独的搜索页面 */
function S_User() {

    var OSname = document.getElementById('Sname');
    var Stext = OSname.value
    var Stype = (Number(Stext))

    /*alert(Stype)*/
    if (isNaN(Stype))
    {
        url = reserver + 'api/search/User/?name=' + Stext
    }
    else
    {
        url = reserver + 'api/search/User/?AccountID=' + Stext
    }

    $.getJSON(url, function (data) {
        var html = '';
        for (var i = 0; i < data.length; i++) {
            html += '<tr>'
            html += '<td>' + data[i].AccountID  + '</td>';
            html += '<td>' + data[i].name + '</td>';
            html += '<td>' + moment(data[i].created_at).format("YYYY-MM-DD h:mm:ss"); + '</td>';
            html += '<td>' + data[i].username + '</td>';
            html += '</tr>'
        }
        $('#Suser').html(html);

    });
}


/*
function getUser() {
    $.getJSON(reserver + "api/v1/User/", function (data) {
        var html = '';
        for (var i = 0; i < data.data.length; i++) {
            html += '<tr>'
            html += '<td>' + data.data[i].AccountID  + '</td>';
            html += '<td>' + data.data[i].name + '</td>';
            html += '<td>' + moment(data.data[i].created_at).format("YYYY-MM-DD h:mm:ss"); + '</td>';
            html += '<td>' + data.data[i].username + '</td>';
            html += '</tr>'
        }
        $('#Guser').html(html);
    });
}
*/






