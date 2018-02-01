/**
 * Created by liushuo on 2018/1/12.
 */
now_projectid = getCookie('now_projectid')


cmd=''

function uncheckAll()
{
    var obj=document.getElementsByName('host'); //选择所有name="'test'"的对象，返回数组
//取到对象数组后，我们来循环检测它是不是被选中
    var s='';
    for(var i=0; i<obj.length; i++){
        if(obj[i].checked) obj[i].checked = false;; //如果选中，将value添加到变量s中
    }

}

function select(name) {
    cmd = name
    $("#cmd").html(cmd);
    $("#cmd1").html(cmd);
    var objresult = document.getElementById('info');
    objresult.innerHTML = '';
    var objip = document.getElementById('host_ip');
    objip.innerHTML = '';
    uncheckAll()
    $("#example-tabs").steps('next');
}
function next() {
    $("#example-tabs").steps('next');
}






function S_host(now_projectid) {
    $.ajax({
        cache: true,
        headers: header,
        type: "get",
        datatype:"json",
        url: reserver + 'api/v1/Product_Host/id/' + now_projectid + '/',
        async: false,
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        error: function (request) {
            alert("Connection error");
        },
        success: function (data) {
            data = data.data
            var html = '';
            for (var i = 0; i < data.length; i++) {
                html += '<input type="checkbox" name="host" value="' + data[i].lan_ip +  '">' + data[i].lan_ip + '</input>';
            }
            html +='<button  onclick="chk()">打印选择</button>'
            $('#host_tree').html(html);


        }
    });
}



function chk(){
    var obj=document.getElementsByName('host'); //选择所有name="'test'"的对象，返回数组
//取到对象数组后，我们来循环检测它是不是被选中
    var s='';
    for(var i=0; i<obj.length; i++){
        if(obj[i].checked) s+=obj[i].value; //如果选中，将value添加到变量s中
    }
//那么现在来检测s的值就知道选中的复选框的值了
    alert(s==''?'你还没有选择任何内容！':s);
    if(s!='') next();
    $('#host_ip').html(s);

}


function  commit() {
    var obj=document.getElementById('cmd1');
    var obj1=document.getElementById('host_ip');
    var info=document.getElementById('info');
    var select_ip = obj1.innerHTML;
    var select_cmd = obj.innerHTML;
    var dataurl = 'api/v1/run_param/?ip=' + select_ip + '&cmd=' + select_cmd;
    result = getdata_req(dataurl,'json','获取执行结果');
    info.innerHTML=result['data'];

}
S_host(now_projectid)


