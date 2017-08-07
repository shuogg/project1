#! usr/bin/python
#coding=utf-8
from django.shortcuts import *
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import *
from django.template import *
from models import *
from admin import *
import datetime,json
import check_code as CheckCode
from view_code import JsonResponse
from view_code import R_Head
from django.template import RequestContext


def check_code(request):
    import io

    stream = io.BytesIO()
    # img图片对象,code在图像中写的内容
    img, code = CheckCode.create_validate_code()
    img.save(stream, "png")
    # 图片页面中显示,立即把session中的CheckCode更改为目前的随机字符串值
    request.session["CheckCode"] = code
    return HttpResponse(stream.getvalue())

    # 代码：生成一张图片，在图片中写文件
    # request.session['CheckCode'] =  图片上的内容

    # 自动生成图片，并且将图片中的文字保存在session中
    # 将图片内容返回给用户

def hello(request):
        return HttpResponse("Hello World")


def check_user(request):

	if request.user:
		users = User.objects.filter(name = request.user) 
		if users: 
			result = R_Head(200)
			print result
			return result
	print request.user
	#return HttpResponse('0')
	result = R_Head(0)
	return result


@login_required
def show_color(request):
	if "favorite_color" in request.COOKIES:
		return HttpResponse("Your favorite color is %s" % request.COOKIES["favorite_color"])
	else:
		return HttpResponse("You don't have a favorite color.")


def check_login(request):

    if request.user.is_authenticated():
        # Do something for authenticated users.
        return HttpResponse("Your Login Success")
    else:
        return HttpResponse("Your Not Login")
        # Do something for anonymous users.

#@app.route('/login', methods=['POST', 'OPTIONS'])
#@crossdomain(origin='*')
def login_v1(request):
	if request.method != 'POST':
		print request.user
		if request.user.is_authenticated():
			#request.META["CSRF_COOKIE_USED"] = True
			return HttpResponse("%s Your Login Success"%request.user)
		else:
    # ... view code here  
			#form=ContactForm()
			#c=RequestContext(request,{'form':form})
			#request.META["CSRF_COOKIE_USED"] = True
			#return render_to_response('login.html',c)
			#request.META["CSRF_COOKIE_USED"] = True
			return render_to_response('login.html')
	else:
		print 'post:',request.POST
	 	#print 'login:',request.POST.get('username', ''), request.POST.get('password', ''),request.POST.get('check_code'),request.session['CheckCode']
		input_code = request.POST.get('check_code')
		print input_code,request.session['CheckCode']
		if input_code.upper() != request.session['CheckCode'].upper():
			print {'message': '验证码错误'}
			result = R_Head(0)
			#return render_to_response('login.html',{'message': '验证码错误'})
			return result
		print 'start auth'
		username = request.POST.get('name', '')
		password = request.POST.get('password', '')
		print 'start auth'
		user = auth.authenticate(name=username, password=password)
		if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
			auth.login(request, user)
			# Redirect to a success page.
			result = R_Head(200)
			print "%s Your Login Success"%request.user
			#print response
			return result
			#return HttpResponse('200')
			#return HttpResponseRedirect("/profile")
		else:
		# Show an error page
    			#return render_to_response('login.html',{'message': 'Sorry, not a valid username or password'})
			result = R_Head(0)
			return result

def logout_v1(request):
	if request.user.is_authenticated():
		out_user=request.user
		print out_user,'start logout'
		auth.logout(request)
	return HttpResponse("%s Your Logout Success"%out_user)


def change_v1(request):
	if request.method != 'POST':
		if request.user.is_authenticated():
			return render_to_response('change.html',{'name':request.user})
		else:
			return render_to_response('change.html')
	else:
		if request.user.is_authenticated():
			username = request.user
			password = request.POST.get('password', '')
			newpassword = request.POST.get('newpassword', '')
			user = auth.authenticate(name=username, password=password)
			print username,password,'reset pass:',newpassword
			if user is not None and user.is_active:
				if len(newpassword)>=8:
					user = User.objects.get(name=request.user)
					user.set_password(newpassword)
					user.save()
					message='%s 成功修改密码'%request.user
					
				else:
					message="新密码不够复杂"
			else:
				message='原密码错误'
			return render_to_response('change.html',{'message': message,'name':request.user,})
		else:	
			message="用户没有登录"
			return render_to_response('change.html',{'message': message})
		


def register_v1(request):
    ret={}
    if request.method == 'POST':
	for i in request.POST:
		ret[i] = request.POST[i]
	print ret
        form = UserCreateForm(request.POST)
	print form.errors
        if form.is_valid():
           new_user = form.save()
           result = R_Head(200)
	   print new_user

           return result
    else:
            form = UserCreateForm()
            if form.is_valid():
		print form
                new_user = form.save()
    		return render_to_response("registration/register.html")
    print 'context1 to form'
    return HttpResponse('0')
    #return render_to_response("registration/register.html", {'ret':ret,'form':form})

def register(request):
    if request.method == 'POST':
	print 'post',request.POST
        form = UserCreateForm(request.POST)
	print form
        if form.is_valid():
           new_user = form.save()
           return HttpResponseRedirect("")
    else:
            form = UserCreateForm()
            if form.is_valid():
                new_user = form.save()
    		return render_to_response("registration/register.html", {'form': form,})
    return render_to_response("registration/register.html", {'form': form,})







@login_required
def profile(request):
    print request.user
    up = User.objects.get(name=request.user)
    print '头像属性:',up.avatar
    return render_to_response('hello.html',{'avatar': up.avatar },context_instance=RequestContext(request))



#return HttpResponse("Your Login Success %s"%request.user.username)

def t1(request):
	return render_to_response('t1.html',{'message': 'I am the second view.'})


