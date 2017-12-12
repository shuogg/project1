/**
 * Created by liushuo on 2017/8/2.
 */
var reserver = 'http://www.91ox.cn:8000/'
var httpserver = 'http://www.91ox.cn/'


now_projectid = getCookie('now_projectid')

function myrefresh() {
    window.location.reload();
}


function  get_data(objurl,dataType,message) {
    $.ajax({
        url:reserver + objurl,
        contentType : "application/x-www-form-urlencoded;charset=utf-8",
        cache: true,
        type: 'get',
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        headers: header,
        async: false,
        dataType : dataType,
        error: function (data) {
            alert('请求错误')
            result='请求错误'


        },
        success: function(data){
            result = data
        }

    })
    return result
}

result = get_data('api/v1/Product_Host/id/'+ now_projectid  + '/','json','获取产品服务器')






$('#tb_Product_Host').bootstrapTable({
    toolbar: "#toolbar",
    idField: "hid",
    pagination: true,
    showRefresh: true,
    search: true,
    clickToSelect: true,
    queryParams: function (param) {
        return {};
    },
    columns: [
        {
    checkbox: true
        },
        {
        field: 'product_id',
        title: 'Product ID'
    }, {
        field: 'product_name',
        title: 'Product Name'
    }, {
        field: 'hid',
        title: 'HID'
    },
        {
        field: 'lan_ip',
        title: '内网IP'
        },
        {
            field:'type',
            title:'类型'
        },
        {
            field:'memory_size',
            title:'内存',
            editable: {
                type: 'text',
                title: '内存',
                validate: function (v) {
                    if (!v) return '内存不能为空';

                }
            }
        },
        {
            field:'disk_size',
            title:'磁盘'
        }

    ],
    data: result.data,
    onEditableSave: function (field, row, oldValue, $el) {
        var hid = row.hid
        $.ajax({
            type: "put",
            url: reserver + "api/v1/Product_Host/" + hid + '/',
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





/*
 /* 删除按钮 */
function ReqDProduct_Host(hid) {
    $.ajax({
        cache: true,
        headers: header,
        type: "DELETE",
        url: reserver + 'api/v1/Product_Host/' + hid + '/',
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
function DProduct_Host() {

    var S_all = $("#tb_Product_Host").bootstrapTable('getAllSelections');
    for (i = 0;i < S_all.length; i++ )
    {
        /*  alert(S_all[i].AccountID) */
        ReqDProduct_Host(S_all[i].hid)
    }


}


/* 编辑和创建按钮  未完成*/
function ReqEProduct_Host(id) {
    alert( $('#EProductHost_Lay').serialize())
    $.ajax({
        data: $('#EProductHost_Lay').serialize(),
        cache: true,
        type: "PUT",
        headers: {'X-CSRFToken': csrftoken },
        url: reserver + 'api/v1/Product_Host/' + hid + '/',
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
function E_Product_Host() {
    S_obj = $("#tb_Product_Host").bootstrapTable('getAllSelections')
    if ( S_obj.length == 1 ) {
        fields = ['product_id','product_name','hid','lan_ip','type','memory_size','disk_size']
        /* alert('getSelections: ' + JSON.stringify(S_obj)) */
        /* JsonId= JSON.stringify(S_obj) */
        var JsonData = S_obj[0]

        var Json_product_id = JsonData.product_id
        var Json_product_name = JsonData.product_name
        var Json_hid = JsonData.hid
        var Json_lan_ip = JsonData.lan_ip
        var Json_type = JsonData.type
        var Json_memory_size = JsonData.memory_size
        var Json_disk_size = JsonData.disk_size
    }
    else
    {
        alert('请勾选一个进行修改')
    }
    /* var html = '<form class="layui-form layui-form-pane" id="EUser_Lay"> <div class="layui-form-item"> <label class="layui-form-label">用户名</label> <div class="layui-input-inline"> <input type="text" name="name" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input" value=' + Json_name + '> </div> </div> <div class="layui-form-item"> <div class="layui-form-item"> <label class="layui-form-label">所属项目</label> <div class="layui-input-inline"> <input type="text" name="project" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input"> <!-- input type="text" name="title" autocomplete="off" placeholder="请输入项目" class="layui-input" --> </div> </div> <div class="layui-form-item"> <div class="layui-input-block"> <input type="button" onclick="ReqEuser(' + Json_AccountID + ')" class="layui-btn layui-btn-primary" value="提交"></input> <input type="reset" class="layui-btn layui-btn-primary"></input> </div> </div> </form>' */
    var html = '<div style="margin: 50px auto; width: 50%"><form class="layui-form layui-form-pane" id="EProductHost_Lay"> <div class="layui-form-item"> <label class="layui-form-label">用户名</label> <div class="layui-input-inline"> <input type="text" name="name" lay-verify="required" placeholder="请输入用户名" autocomplete="off" class="layui-input" value=' + Json_name + '> </div> </div> <div class="layui-form-item"><label class="layui-form-label">用户昵称</label> <div class="layui-input-inline"> <input type="text" name="username" lay-verify="required" placeholder="请输入昵称" autocomplete="off" class="layui-input" value=' + Json_username + '> </div> </div>  <div class="layui-form-item"> <div class="layui-form-item"> <label class="layui-form-label">所属项目</label> <div class="layui-input-inline"> <input type="text" name="project" lay-verify="required" placeholder="请输入项目" autocomplete="off" class="layui-input">  </div> </div> <div class="layui-form-item"> <div class="layui-input-block"> <input type="button" onclick="ReqEProduct_Host(' + Json_AccountID + ')" class="layui-btn layui-btn-primary" value="提交"></input> <input type="reset" class="layui-btn layui-btn-primary"></input> </div> </div> </form></div>'
    E_E_LayProduct_Host(html)
}
function E_LayProduct_Host(html){
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

        ,C_Host: function(){
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
                ,content:'<div style="margin: 50px auto; width: 50%"><form class="layui-form layui-form-pane" id="CProductHost_Lay"> <div class="layui-form-item" > <label class="layui-form-label">用户名</label> <div class="layui-input-inline"> <input type="text" name="name" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input"> <!-- input type="text" name="title" autocomplete="off" placeholder="请输入登录名" class="layui-input" --> </div> </div> <div class="layui-form-item"> <label class="layui-form-label">密码</label> <div class="layui-input-inline"> <input type="password" name="password1" placeholder="请输入密码" autocomplete="off" class="layui-input"> </div> <div class="layui-form-mid layui-word-aux">请务必填写用户名</div> </div> <div class="layui-form-item"> <label class="layui-form-label">确认密码</label> <div class="layui-input-inline"> <input type="password" name="password2" placeholder="请输入密码" autocomplete="off" class="layui-input"> </div> <div class="layui-form-mid layui-word-aux">请务必填写用户名</div> </div> <div class="layui-form-item"> <label class="layui-form-label">所属项目</label> <div class="layui-input-inline"> <input type="text" name="project" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input"> <!-- input type="text" name="title" autocomplete="off" placeholder="请输入登录名" class="layui-input" --> </div> </div> <div class="layui-form-item"> <div class="layui-input-block"> <input type="button" onclick="CUser_Lay()" class="layui-btn layui-btn-primary" value="提交"></input> <input type="reset" class="layui-btn layui-btn-primary"></input> </div> </div> </form></div>'
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
        ,confirmTrans_DHost: function(){
            //配置一个透明的询问框
            layer.msg('你确认要进行删除吗', {
                time: 20000, //20s后自动关闭
                btn: ['知道了',"<span onclick='DProduct_Host()'>确认删除</span>"]});
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

var OE_Product_Host = document.getElementById('btn_Hostedit')
OE_Product_Host.onclick = E_Product_Host








