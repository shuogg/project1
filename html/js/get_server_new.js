/**
 * Created by liushuo on 2017/8/1.
 */
var reserver = 'http://192.168.137.1:8000/'
var httpserver = 'http://192.168.137.1:90/'

function myrefresh() {
    window.location.reload();
}

function setCookie(name,value)
{
    var Days = 30;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days*24*60*60*1000);
    document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString();
}

function getProject(name)
{
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
    if(arr=document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return false;
}

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




function  Insert_Name() {
    var Oname = document.getElementById('vname');
    try {
        Oname.innerHTML = ' <li class="layui-nav-item"  style="float: right"><span  id="logout">&nbsp;&nbsp;退出</span></li><li class="layui-nav-item" style="float: right">' + name + '</li> '
        window.onload = function () {
            var Ologout = document.getElementById('logout')
            Ologout.onclick = logout
        }
    }
    catch (e) {
        window.location.href= httpserver + 'index.html'
    }

}






function  get_req(objurl,dataType,message) {
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

        },
        success: function(data){
            if (data.status == '0')
            {
                window.location.href= httpserver + 'login.html';
            }
            if (data.status == '200')
            {
                if (message != '登出') {
                    Insert_Name()
                    Init_Project()
                }

                /* alert(message + '成功') */
            }
        }

    })

}

function   post_req(ojburl,data,dataType,message) {
    $.ajax({
        contentType : "application/x-www-form-urlencoded;charset=utf-8",
        cache: true,
        type: "POST",
        url: reserver + ojburl,
        data: data,// 你的formid
        async: false,
        dataType: dataType,
	headers: header,
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        error: function (data) {
            alert('请求失败')
            result =  false
        },
        success: function(data){
            if (data.status == "200" || data.code == 200)
            {
                alert(message + '成功')
                result = true;
            }
            else
            {
                alert(message + '失败')
                result = false;
            }

        }


    });
    return result;

}



function check_login() {
    get_req('check_user','json','检查登录')
}



function login() {
    result =  post_req('login',$('#Login').serialize(),'json','登录')
    if (result) {
        var namev = document.getElementById('name')
        name = namev.value
        window.location.href= httpserver + 'index.html'
    }

}

function logout() {
    delete name;
    get_req('logout','json','登出')
    window.location.href= httpserver + 'login.html';


}



function create_user() {
    result = post_req('register',$('#Cuser').serialize(),'json','注册')
}

function CUser_Lay() {
    result = post_req('register',$('#CUser_Lay').serialize(),'json','注册')
    if (result) {
        layer.closeAll()
        myrefresh()
    }
}

function CProduct_Lay() {
    result = post_req('api/v1/Product/',$('#CProduct_Lay').serialize(),'json','新建项目')
    if (result) {
        layer.closeAll()
        myrefresh()
    }
}

function CServer_Lay() {
    alert($('#CProductServer_Lay').serialize())
    result = post_req('api/v1/Product_Server/',$('#CProductServer_Lay').serialize(),'json','新建项目')
    if (result) {
        layer.closeAll()
        myrefresh()
    }
}

function CProductHost_Lay() {
    alert($('#CProductHost_Lay').serialize())
    result = post_req('api/v1/Product_Host/',$('#CProductHost_Lay').serialize(),'json','新建服务器')
    if (result) {
        layer.closeAll()
        myrefresh()
    }
}



function isStr(s)
{
    var patrn=/^[a-z]{1,20}$/;
    if (!patrn.exec(s)) return false
    return true
}

function hasClass( elements,cName ){
    return !!elements.className.match( new RegExp( "(\\s|^)" + cName + "(\\s|$)") ); // ( \\s|^ ) 判断前面是否有空格 （\\s | $ ）判断后面是否有空格 两个感叹号为转换为布尔值 以方便做判断
};

function removeClass( elements,cName ) {
    if (hasClass(elements, cName)) {
        elements.className = elements.className.replace(new RegExp("(\\s|^)" + cName + "(\\s|$)"), " "); // replace方法是替换
    }
    ;
}
function addClass( elements,cName ){
    if( !hasClass( elements,cName ) ){
        elements.className += " " + cName;
    };
};
