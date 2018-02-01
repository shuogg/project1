/**
 * Created by liushuo on 2017/8/2.
 */
var reserver = 'http://192.168.137.1:8000/'
var httpserver = 'http://192.168.137.1:90/'


now_projectid = getCookie('now_projectid')




function  get_data(objurl,data,dataType,message) {
    $.ajax({
        url:reserver + objurl,
        contentType : "application/x-www-form-urlencoded;charset=utf-8",
        cache: true,
        data:data,
        type: 'get',
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        headers: header,
        async: false,
        dataType : dataType,
        error: function (output) {
            alert(data.argv + '请求失败')
            result={data : data.argv + '请求失败'}


        },
        success: function(data){
            result = data
        }

    })
    return result
}

result = get_data('api/v1/Product_Server/id/'+ now_projectid  + '/','','json','获取产品服务器')






$('#tb_Product_job').bootstrapTable({
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
});




function  run_cmd() {

    var out = '执行结果:<br>';
    var obj=document.getElementById('input_cmd');
    var cmd=obj.value;
    var S_all = $("#tb_Product_job").bootstrapTable('getAllSelections');
    var info_result=document.getElementById('info_result');
    info_result.innerHTML=''
    if (S_all.length == 0 )
    {
        alert('请选择需要执行命令的服务器')
    }
    for (i = 0;i < S_all.length; i++ )
    {
        var data={cmd:cmd,argv:S_all[i].server_id};
        var dataurl = 'api/v1/run_param/';
        /* var dataurl = 'api/v1/run_param/?cmd=' + cmd + '&argv=' + S_all[i].server_id; */
        /* result = getdata_req(dataurl,'json','获取执行结果'); */
        result = get_data(dataurl,data,'json','获取执行结果');
        out+=result['data'] + '<br>';
        info_result.innerHTML=out
        /* ReqDProduct_Server(S_all[i].server_id) */
    }
    /* info_result.innerHTML=out */


}






