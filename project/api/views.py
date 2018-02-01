#coding=utf-8
from django.shortcuts import render
from rest_framework import generics
from p1.tables import *
import sys,os
from api.serializers import *
from rest_framework import permissions,status
from api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from django.http import *
# Create your views here.
from rest_framework.views import exception_handler
from rest_framework.response import Response
from p1.view_code import JsonResponse
from django.shortcuts import get_object_or_404 
import importlib 
from p1.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from job import push_zk as push_zk

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['code'] = response.status_code
        response.data['message'] = response.data['detail']
        #response.data['data'] = None
        del response.data['detail'] 

    return response


def get_active(request):
	result = push_zk.get('1')
	print result
	return HttpResponse(result)



class UserList(LoginRequiredMixin,APIView):
	login_url = '/login'
	#permission_classes = (permissions.AllowAny)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly)
	def get(self, request,format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='') 
		#return Response(serializer.data)
	def post(self, request, format=None):
		print '6'
		serializer = UserSerializer(data=request.data)
		password = self.request.POST.get('password')
		if serializer.is_valid():
			serializer.save(password = make_password(password))
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
			#return Response(serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(data=serializer.errors, code=status.HTTP_400_BAD_REQUEST, message='')
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetail(LoginRequiredMixin,APIView):
	#permission_classes = (permissions.AllowAny)
	permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticatedOrReadOnly,)
	def get_object(self, pk):
		#house = get_object_or_404(House, pk=house_pk)
		return get_object_or_404(User,pk=pk)
		'''
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			return
		''' 
	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		#return Response(serializer.data)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
	def put(self, request, pk, format=None):
		print '2'
		user = self.get_object(pk)
		print request
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			if 'password' in self.request.POST:
				uquery = User.objects.get(name = self.request.POST.get('name'))
				password = self.request.POST.get('password')
				uquery.set_password = password
			serializer.save()
			#return Response(serializer.data)
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return JsonResponse(data=serializer.errors, code=status.HTTP_400_BAD_REQUEST, message='')
	def delete(self, request, pk, format=None):
		print request 
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)





class TbNameList(LoginRequiredMixin,APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	def get(self, request,TbName,format=None):
		try:
			m0 =importlib.import_module('p1.tables')
			TbClass = getattr(m0,TbName)
			m1 =importlib.import_module('api.serializers')
			SeClass = getattr(m1,TbName + 'Serializer')
			TbObjects = TbClass.objects.all()
			o = User.objects.get(name=request.user)
			#print o.Product.all()
			#if TbName == 'Product':
				#print TbName,request.user,User.objects.get(name = request.user).AccountID
			#	TbObjects = TbClass.objects.filter(owner_id = User.objects.get(name = request.user).AccountID)
			#	print TbObjects
			serializer = SeClass(TbObjects, many=True)
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='') 
		except:
			return JsonResponse(data='', code='0', message='不存在') 

	def post(self, request,TbName,format=None):
		#try:
			m1 =importlib.import_module('api.serializers')
			SeClass = getattr(m1,TbName + 'Serializer')
			serializer = SeClass(data=request.data)
			#print request.data
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
				#return Response(serializer.data, status=status.HTTP_201_CREATED)
			return JsonResponse(data=serializer.errors, code=status.HTTP_400_BAD_REQUEST, message='')
		#except:
		#	return JsonResponse(data='', code='0', message='不存在') 

class TbNameDetail(LoginRequiredMixin,APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	def get_object(self, TbName,pk):
		m0 =importlib.import_module('p1.tables')
		TbClass = getattr(m0,TbName)
		#house = get_object_or_404(House, pk=house_pk)
		return get_object_or_404(TbClass,pk=pk)
		'''
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			return
		''' 
	def get(self, request, TbName,pk, format=None):
		user = self.get_object(TbName,pk)
		m1 =importlib.import_module('api.serializers')
		SeClass = getattr(m1,TbName + 'Serializer')
		serializer = SeClass(user)
		#return Response(serializer.data)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
	def put(self, request, TbName,pk, format=None):
		user = self.get_object(TbName,pk)
		print request.data
		m1 =importlib.import_module('api.serializers')
		SeClass = getattr(m1,TbName + 'Serializer')
		serializer = SeClass(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			#return Response(serializer.data)
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return JsonResponse(data=serializer.errors, code=status.HTTP_400_BAD_REQUEST, message='')
	def delete(self, request, TbName,pk, format=None):
		user = self.get_object(TbName,pk)
		user.delete()
		return JsonResponse(data='delete ok', code=status.HTTP_200_OK, message='')


class ProductList(LoginRequiredMixin,APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	def get(self, request,format=None):
		try:
			TbName = 'Product'
			m0 =importlib.import_module('p1.tables')
			TbClass = getattr(m0,TbName)
			m1 =importlib.import_module('api.serializers')
			SeClass = getattr(m1,TbName + 'Serializer')
			TbObjects = TbClass.objects.all()
			o = User.objects.get(name=request.user)
			TbObjects = o.Product.all()
			#if TbName == 'Product':
				#print TbName,request.user,User.objects.get(name = request.user).AccountID
			#	TbObjects = TbClass.objects.filter(owner_id = User.objects.get(name = request.user).AccountID)
			#	print TbObjects
			serializer = SeClass(TbObjects, many=True)
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='') 
		except:
			return JsonResponse(data='', code='0', message='不存在') 
	def post(self, request, format=None):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
			#return Response(serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(data=serializer.errors, code=status.HTTP_400_BAD_REQUEST, message='')
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TbNameIdList(LoginRequiredMixin,APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	def get(self, request,TbName,product_id):
		try:
			m0 =importlib.import_module('p1.tables')
			TbClass = getattr(m0,TbName)
			m1 =importlib.import_module('api.serializers')
			SeClass = getattr(m1,TbName + 'Serializer')
			TbObjects = TbClass.objects.filter(product_id = product_id)
			o = User.objects.get(name=request.user)
			#if TbName == 'Product':
				#print TbName,request.user,User.objects.get(name = request.user).AccountID
			#	TbObjects = TbClass.objects.filter(owner_id = User.objects.get(name = request.user).AccountID)
			#	print TbObjects
			serializer = SeClass(TbObjects, many=True)
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='') 
		except:
			return JsonResponse(data='', code='0', message='不存在') 

class run_cmd(LoginRequiredMixin,APIView):
	#permission_classes = (permissions.AllowAny)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	def get(self,request,cmd):
		print cmd,request.data
		cmd_out=os.popen(cmd)
		result =  cmd_out.read().rstrip('\n')
		data = result.decode('gb2312')
		#return HttpResponse(data)
		return JsonResponse(data='%s'%data, code=status.HTTP_200_OK, message='') 


class run_param(LoginRequiredMixin,APIView):
	#permission_classes = (permissions.AllowAny)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	def get(self,request):
		#cmd_out=os.popen(cmd)
		#result =  cmd_out.read().rstrip('\n')
		#data = result.decode('gb2312')
		#print request.data
		cmd = request.GET.get('cmd')
		cmd_argv = request.GET.get('argv')
		print cmd,cmd_argv
		result = os.popen('%s %s'%(cmd,cmd_argv))
		print 'cmd_result',result
		data = result.read().decode('gb2312')
		print 'response',data
		#return HttpResponse(data)
		return JsonResponse(data='%s'%data, code=status.HTTP_200_OK, message='') 


def exec_command(comm):
    hostname = '192.168.137.132'
    username = 'root'
    password = '登陆的Linux账号密码'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(comm)
    result = stdout.read()
    ssh.close()
    return result


from dwebsocket import require_websocket,accept_websocket
import subprocess
from subprocess import PIPE,Popen,STDOUT
@require_websocket
def echo_once(request):
    message = request.websocket.wait()

@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request,'index.html')
    else:
    	'''result = os.popen('VER')
	data = result.read()
	print type(data),
	output_result = data.rstrip('\n')'''
	for message in request.websocket:
		subp = subprocess.Popen(['ping', 'www.baidu.com', '-n', '3'], stdout = subprocess.PIPE)
		print message
		#print message
		'''subp = subprocess.Popen(['python','-c','haha.txt'], stdout = subprocess.PIPE)'''
		c=subp.stdout.readline()
		while c:
			print c
			request.websocket.send(c.decode('gb2312').encode('utf-8'))
			c=subp.stdout.readline()
		print 'Done'
		'''request.websocket.send(output_result.decode('gb2312').encode('utf-8'))'''
		


'''
class UserList(generics.ListCreateAPIView):
	message = User.objects.all()
	queryset = message
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

	def perform_create(self, serializer):
		password = self.request.POST.get('password')
		serializer.save(password = make_password(password))

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)	
	queryset = User.objects.all()
	serializer_class = UserSerializer


	def perform_update(self, serializer):
		if 'password' in self.request.POST:
			uquery = User.objects.get(name = self.request.POST.get('name'))
			password = self.request.POST.get('password')
			uquery.set_password = password
		else:
			serializer.save()
'''

'''
class Product_HostList(LoginRequiredMixin,APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	def get(self, request,product_id):
		try:
			TbName = 'Product_Host'
			m0 =importlib.import_module('p1.tables')
			TbClass = getattr(m0,TbName)
			m1 =importlib.import_module('api.serializers')
			SeClass = getattr(m1,TbName + 'Serializer')
			TbObjects = TbClass.objects.filter(product_id = product_id)
			#if TbName == 'Product':
				#print TbName,request.user,User.objects.get(name = request.user).AccountID
			#	TbObjects = TbClass.objects.filter(owner_id = User.objects.get(name = request.user).AccountID)
			#	print TbObjects
			serializer = SeClass(TbObjects, many=True)
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='') 
		except:
			return JsonResponse(data='', code='0', message='不存在') 


class Product_cmdList(LoginRequiredMixin,APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	def get(self, request,product_id):
		try:
			print 'hehe'
			TbName = 'Product_cmd'
			m0 =importlib.import_module('p1.tables')
			TbClass = getattr(m0,TbName)
			m1 =importlib.import_module('api.serializers')
			SeClass = getattr(m1,TbName + 'Serializer')
			TbObjects = TbClass.objects.filter(product_id = product_id)
			print TbObjects
			#if TbName == 'Product':
				#print TbName,request.user,User.objects.get(name = request.user).AccountID
			#	TbObjects = TbClass.objects.filter(owner_id = User.objects.get(name = request.user).AccountID)
			#	print TbObjects
			serializer = SeClass(TbObjects, many=True)
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='') 
		except:
			return JsonResponse(data='', code='0', message='不存在') 


'''