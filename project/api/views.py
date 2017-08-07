#coding=utf-8
from django.shortcuts import render
from rest_framework import generics
from p1.tables import *
import sys
from api.serializers import *
from rest_framework import permissions,status
from api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
# Create your views here.
from rest_framework.views import exception_handler
from rest_framework.response import Response
from p1.view_code import JsonResponse
from django.shortcuts import get_object_or_404 
import importlib 
from p1.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

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

class AccountsList(APIView):
	#permission_classes = (IsOwnerOrReadOnly,permissions.AllowAny)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)	
	def get(self, request,format=None):
		accounts = Accounts.objects.all()
		print accounts
		serializer = AccountsSerializer(accounts, many=True)
		return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='') 
		#return Response(serializer.data)
	def post(self, request, format=None):
		serializer = AccountsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
			#return Response(serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(data=serializer.errors, code=status.HTTP_400_BAD_REQUEST, message='')
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserList(LoginRequiredMixin,APIView):
	login_url = '/login'
	#permission_classes = (permissions.AllowAny)
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	def get(self, request,format=None):
		print '哦哦'
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



class UserDetail(APIView):
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
		print '1'
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



class TbNameList(APIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
	def get(self, request,TbName,format=None):
		try:
			m0 =importlib.import_module('p1.tables')
			TbClass = getattr(m0,TbName)
			m1 =importlib.import_module('api.serializers')
			SeClass = getattr(m1,TbName + 'Serializer')
			TbObjects = TbClass.objects.all()
			serializer = SeClass(TbObjects, many=True)
			return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='') 
		except:
			return JsonResponse(data='', code='0', message='不存在') 

	def post(self, request,TbName,format=None):
		#try:
			m1 =importlib.import_module('api.serializers')
			SeClass = getattr(m1,TbName + 'Serializer')
			serializer = SeClass(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(data=serializer.data, code=status.HTTP_200_OK, message='')
				#return Response(serializer.data, status=status.HTTP_201_CREATED)
			return JsonResponse(data=serializer.errors, code=status.HTTP_400_BAD_REQUEST, message='')
		#except:
		#	return JsonResponse(data='', code='0', message='不存在') 

class TbNameDetail(APIView):
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

