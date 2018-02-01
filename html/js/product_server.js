/**
 * Created by liushuo on 2017/8/2.
 */
var reserver = 'http://192.168.137.1:8000/'
var httpserver = 'http://192.168.137.1:90/'


now_projectid = getCookie('now_projectid')




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

result = get_data('api/v1/Product_Server/id/'+ now_projectid  + '/','json','获取产品服务器')






$('#tb_Product_Server').bootstrapTable({
    toolbar: "#toolbar",
    idField: "hid",
    pagination: true,
    showRefresh: true,
    search: true,
    clickToSelect: true,
    showExport: true,
    exportDataType: "all",
    queryParams: function (param) {
        return {};
    },
    columns: [
        {
            checkbox: true
        },
        {
            field: 'server_id',
            title: 'server_id',
            sortable : true,
        }, {
            field: 'server_name',
            title: 'server_name',
            editable: {
                type: 'text',
                title: '区组名称',
                validate: function (v) {
                    if (!v) return '区组名称不能为空';

                }
            }
        },
        {
            field: 'server_ip',
            title: '服务器IP'
        },
        {
            field: 'hid',
            title: 'HID',
            sortable : true,
        },
        {
            field:'server_type',
            title:'区组类型'
        },
        {
            field: 'open_time',
            title: '开服时间',
        },
        {
            field: 'product_id',
            title: '项目ID',
        }


    ],
    data: result.data,
    onEditableSave: function (field, row, oldValue, $el) {
        var server_id = row.server_id
        $.ajax({
            type: "put",
            url: reserver + "api/v1/Product_Server/" + server_id + '/',
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










var add_html = '<div style="margin: 50px auto; width: 50%"> <form class="layui-form layui-form-pane" id="CProductServer_Lay"> <div class="layui-form-item" > <label class="layui-form-label">区组ID</label> <div class="layui-input-block"> <input type="text" name="server_id" lay-verify="required" placeholder="请输入区组ID" autocomplete="off" class="layui-input"> </div> </div> <div class="layui-form-item" > <label class="layui-form-label">区组名称</label> <div class="layui-input-block"> <input type="text" name="server_name" lay-verify="required" placeholder="请输入区组名称" autocomplete="off" class="layui-input"> </div> </div> <div class="layui-form-item" > <label class="layui-form-label">区组类型</label> <div class="layui-input-block"> <input type="text" name="server_type" lay-verify="required" placeholder="请输入区组类型" autocomplete="off" class="layui-input"> </div> </div> <div class="layui-form-item" > <label class="layui-form-label">服务器IP</label> <div class="layui-input-block"> <input type="text" name="server_ip" lay-verify="required" placeholder="请输入服务器IP" autocomplete="off" class="layui-input"> </div> </div> <div class="layui-form-item" > <label class="layui-form-label">项目ID</label> <div class="layui-input-block"> <input type="text" name="product_id" lay-verify="required" placeholder="请输入项目ID" autocomplete="off" class="layui-input"> </div> </div> <div class="layui-form-item" > <label class="layui-form-label">项目名称</label> <div class="layui-input-block"> <input type="text" name="product_name" lay-verify="required" placeholder="请输入项目名称" autocomplete="off" class="layui-input"> </div> </div> <div class="layui-form-item" > <label class="layui-form-label">服务器HID</label> <div class="layui-input-block"> <input type="text" name="hid" lay-verify="required" placeholder="请输入服务器HID" autocomplete="off" class="layui-input"> </div> </div> <div class="layui-form-item" > <label class="layui-form-label">开服时间</label> <div class="layui-input-block"> <input type="text" name="open_time" lay-verify="required" placeholder="请输入开服时间" autocomplete="off" class="layui-input"> </div> </div> <div class="layui-form-item"> <div class="layui-input-block"> <input type="button" onclick="CServer_Lay()" class="layui-btn layui-btn-primary" value="提交"> <input type="reset" class="layui-btn layui-btn-primary"></input> </div> </div></form> </div>'
/*
 /* 删除按钮 */
function ReqDProduct_Server(server_id) {
    $.ajax({
        cache: true,
        headers: header,
        type: "DELETE",
        url: reserver + 'api/v1/Product_Server/' + server_id + '/',
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
function DProduct_Server() {

    var S_all = $("#tb_Product_Server").bootstrapTable('getAllSelections');
    for (i = 0;i < S_all.length; i++ )
    {
        /*  alert(S_all[i].AccountID) */
        ReqDProduct_Server(S_all[i].server_id)
    }


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

        ,C_Server: function(){
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
                ,content:add_html
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
        ,confirmTrans_DServer: function(){
            //配置一个透明的询问框
            layer.msg('你确认要进行删除吗', {
                time: 20000, //20s后自动关闭
                btn: ['知道了',"<span onclick='DProduct_Server()'>确认删除</span>"]});
        }

    };

    $('.site-demo-button .layui-btn').on('click', function(){
        var othis = $(this), method = othis.data('method');
        active[method] ? active[method].call(this, othis) : '';
    });

});



