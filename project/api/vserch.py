from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from p1.tables import *
from api.serializers import *
from rest_framework import permissions,status
from api.permissions import IsOwnerOrReadOnly
from rest_framework.views import exception_handler
from rest_framework.response import Response
from p1.view_code import JsonResponse
from django.shortcuts import get_object_or_404 
import importlib 
from p1.models import User


class UserSearch(generics.ListAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)	
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('name','AccountID')


class AccountsSearch(generics.ListAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)	
	queryset = Accounts.objects.all()
	serializer_class = UserSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('UserName','Account_id')
