/**
 * Created by liushuo on 2017/8/9.
 */
check_login()
function myrefresh() {
    window.location.reload();
}
var OP_ul = document.getElementById('p_ul');
var OP_li = OP_ul.getElementsByTagName('a');
var OP_btn = document.getElementById('p_btn')
for (var i = 0; i < OP_li.length; i++) {
        OP_li[i].onclick = function () {
            OP_btn.innerHTML = this.innerHTML + '&nbsp&nbsp&nbsp&nbsp<span class="caret"></span>'
            now_project = this.innerHTML
            setCookie('now_project',now_project)
            now_projectid = project_list[now_project]
            setCookie('now_projectid',now_projectid)
            myrefresh()
            /*alert(now_project)
            alert(now_projectid)
            */
        }
}
function  Init_Project() {
    project_list = Product_List()
    var OPul = document.getElementById('p_ul')
    var OPbtn = document.getElementById('p_btn')
    var projectObj = new Array();
    var ul_str = ''
    for (var o in project_list)
    {
        ul_str += '<li><a href="javascript:;">'  + o + '</a></li>'
        projectObj.push(o)
    }
    var html = ul_str
    default_project =  getProject('now_project')
    if (default_project == false) {
        OPbtn.innerHTML =  'projectObj[0] '  +'&nbsp&nbsp&nbsp&nbsp'  +  OPbtn.innerHTML
    }
    else
    {
        OPbtn.innerHTML =  default_project  +'&nbsp&nbsp&nbsp&nbsp'  +  OPbtn.innerHTML

    }
    OPul.innerHTML = html
}

