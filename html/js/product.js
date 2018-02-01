/**
 * Created by liushuo on 2017/8/8.
 */
var reserver = 'http://192.168.137.1:8000/'
var httpserver = 'http://192.168.137.1:90/'


var csrftoken = getCookie('csrftoken');

header = {'X-CSRFToken': csrftoken }

function  getdata_req(objurl,dataType,message) {
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
                    result = data

        }

    })
    return result

}

function Product_List() {
    result =  getdata_req('api/v1/Product/','json','获取产品列表')
    project_list = {}
    if ( 'error' != result) {
        for (var i = 0; i < result.data.length ; i ++ )
        {
            project_list[result.data[i].product_name] = result.data[i].product_id
        }
    }
    return project_list
}










