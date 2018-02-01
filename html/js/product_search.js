/**
 * Created by liushuo on 2017/8/2.
 */
var reserver = 'http://192.168.137.1:8000/'
var httpserver = 'http://192.168.137.1:90/'


function  getproduct_req(objurl,dataType,message) {
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
            alert(message + '请求错误')
            result = 'error'

        },
        success: function(data){
            var obj = [];
            $.each(data.data, function(i, d) {

                obj.push(d);
                // alert(obj.coursename);
            });
            result = obj

        }

    })
    return result

}





var result =  getproduct_req('api/v1/Product/','json','获取产品列表')

function myrefresh() {
    window.location.reload();
}




/* product_serch_ad init */

$(function () {
    $("#tb_product").bootstrapTable({
        toolbar: "#toolbar",
        idField: "Id",
        pagination: true,
        showRefresh: true,
        search: true,
        clickToSelect: true,
        queryParams: function (param) {
            return {};
        },
        data:result,
        columns: [{
            checkbox: true
        },
            {
                field: "product_id",
                title: "产品ID",
                sortable : true,
            }
            ,{
                field: "product_name",
                title: "产品名称",
                editable: {
                    type: 'text',
                    title: '产品名称',
                    validate: function (v) {
                        if (!v) return '用户名不能为空';

                    }
                }
            }, {
                field: "owner",
                title: "用户id",
                sortable : true,
            },],

        onEditableSave: function (field, row, oldValue, $el) {
            var id = row.product_id
            $.ajax({
                type: "put",
                url: reserver + "api/v1/Product/" + id + '/',
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



/* add */



/* delete */

function ReqDProduct(id) {
    $.ajax({
        cache: true,
        headers: header,
        type: "DELETE",
        url: reserver + 'api/v1/Product/' + id + '/',
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
function D_Product() {

    var S_all = $("#tb_product").bootstrapTable('getAllSelections');
    for (i = 0;i < S_all.length; i++ )
    {
        /*  alert(S_all[i].AccountID) */
        ReqDProduct(S_all[i].product_id)
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

        ,C_Product: function(){
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
                ,content:'<div style="margin: 50px auto; width: 50%"><form class="layui-form layui-form-pane" id="CProduct_Lay"> <div class="layui-form-item" > <label class="layui-form-label">产品ID</label> <div class="layui-input-inline"> <input type="text" name="product_id" lay-verify="required" placeholder="请输入产品ID" autocomplete="off" class="layui-input"> <!-- input type="text" name="title" autocomplete="off" placeholder="请输入登录名" class="layui-input" --> </div> </div> <div class="layui-form-item"> <label class="layui-form-label">产品名称</label> <div class="layui-input-inline"> <input type="text" name="product_name" placeholder="请输入产品名称" autocomplete="off" class="layui-input"> </div>    <div class="layui-form-mid layu </div> <div class="layui-form-item"> <label class="layui-form-label">所属用户ID</label> <div class="layui-input-inline"> <input type="text" name="owner" lay-verify="required" placeholder="请输入" autocomplete="off" class="layui-input"> <!-- input type="text" name="title" autocomplete="off" placeholder="请输入登录名" class="layui-input" --> </div> </div> <div class="layui-form-item"> <div class="layui-input-block"> <input type="button" onclick="CProduct_Lay()" class="layui-btn layui-btn-primary" value="提交"></input> <input type="reset" class="layui-btn layui-btn-primary"></input> </div> </div> </form></div>'
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
        ,confirmTrans_Product: function(){
            //配置一个透明的询问框
            layer.msg('你确认要进行删除吗', {
                time: 20000, //20s后自动关闭
                btn: ['知道了',"<span onclick='D_Product()'>确认删除</span>"]});
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


