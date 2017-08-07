#coding=utf-8
from p1.models import User
from p1.tables import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from p1.tables import *
import datetime




class UserSerializer(serializers.Serializer):
	AccountID = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=11)
	username = serializers.CharField(max_length=10,allow_blank = True)
	password = serializers.CharField(max_length=20)
	channel = models.IntegerField()
	from_id = serializers.CharField(max_length=11)
	token = serializers.CharField(max_length=20)
	time = serializers.CharField(max_length=20)


	def create(self, validated_data):
		return User.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.user = validated_data.get('user', instance.user)
		instance.username = validated_data.get('username', instance.username)
		instance.password = validated_data.get('password',instance.password)
		instance.save()
		return instance
		



class UserSerializer(serializers.ModelSerializer):
	#snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = User
		fields = ('AccountID', 'name', 'username','channel','from_id','time','created_at')
		#fields = ('name','username')



class AccountsSerializer(serializers.Serializer):
	Account = models.ForeignKey('p1.User',related_name='Accounts')#账号ID
	AccountName = models.CharField(max_length=10)	#账号名
	AccountLevelCode = models.IntegerField(default=0)	 # 账号级别
	UserID = models.IntegerField()	#身份证号码
	UserName = models.CharField(max_length=10)	#姓名
	GenderCode = models.IntegerField(default=0)	#性别
	UserImgURL = models.URLField()	#身份证照
	RegisterDate = models.DateTimeField()	#注册日期
	JoinIP = models.CharField(max_length=39)	#注册IP
	ChannelCode = models.IntegerField()	#渠道ID/邀请人ID
	def create(self, validated_data):
		return Accounts.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.AccountName = validated_data.get('AccountName', instance.AccountName)
		instance.GenderCode = validated_data.get('GenderCode', instance.GenderCode)
		instance.ChannelCode = validated_data.get('ChannelCode',instance.ChannelCode)
		instance.save()
		return instance

class AccountsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Accounts
		fields = ('Account', 'AccountName', 'AccountLevelCode','UserID','UserName','GenderCode','JoinIP','RegisterDate','ChannelCode')




class AccountStatusSerializer(serializers.Serializer):
	Account = models.ForeignKey('p1.User',related_name='AccountStatus') 	##账号ID
	AccountStatus = models.IntegerField(default=0) #账号状态
	NameAuthStatus = models.IntegerField(default=0) #实名认证状态
	ContactStatus = models.IntegerField(default=0) #通讯录审核状态
	CarrierAuthStatus = models.IntegerField(default=0) #运营商认证状态
	DeviceAuthStatus = models.IntegerField(default=0) #设备验证状态
	BankCardAuthStatus = models.IntegerField(default=0) #银行卡绑定状态

	def create(self, validated_data):
		return AccountStatus.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.AccountStatus = validated_data.get('AccountStatus', instance.AccountStatus)
		instance.ContactStatus= validated_data.get('ContactStatus', instance.ContactStatus)
		instance.CarrierAuthStatus = validated_data.get('CarrierAuthStatus',instance.CarrierAuthStatus)
		instance.save()
		return instance





class AccountInfoSerializer(serializers.Serializer):	
	account = models.ForeignKey('p1.User',related_name='AccountInfo') 	##账号ID
	ProfileImgURL = models.URLField()	#账号头像
	NickName = models.CharField(max_length=10)	#账号昵称
	PhoneNumber = models.IntegerField()	#手机号
	CarrierCode = models.IntegerField(default=0)	#运营商代码
	InviterID = models.IntegerField()	#邀请人ID
	Address	= models.CharField(max_length=30) #地址
	Mail = models.EmailField() #邮箱

	def create(self, validated_data):
		return AccountInfo.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.NickName = validated_data.get('user', instance.NickName)
		instance.PhoneNumber = validated_data.get('username', instance.PhoneNumber)
		instance.InviterID= validated_data.get('InviterID',instance.InviterID)
		instance.save()
		return instance


class DevicesSerializer(serializers.Serializer):
	account = models.ForeignKey('p1.User',related_name='Devices')  #账号ID
	device_id = models.IntegerField(null=False)      #设备ID
	udid = models.IntegerField(null=False)          #设备唯一识别码
	device_name = models.CharField(max_length=30)    #设备名称
	device_mode = models.CharField(max_length=30)   #设备型号
	system_version = models.CharField(max_length=10)  #系统版本
	app_version = models.CharField(max_length=10)        #设备截图
	jail_broken = models.IntegerField(default=0) #越狱状态
	access_gps = models.CharField(max_length=30)
	token = models.CharField(max_length=30)
	time = models.DateField()      #最后登录时间
	def create(self, validated_data):
		return Devices.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.device_id = validated_data.get('device_id', instance.device_id)
		instance.device_name= validated_data.get('device_name', instance.device_name)
		instance.system_version= validated_data.get('system_version',instance.system_version)
		instance.save()
		return instance



