#! usr/bin/python 
#coding=utf-8
from django.db import models
class Accounts(models.Model):
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
	class Meta:
		db_table = 'Accounts'

class AccountStatus(models.Model):
	Account = models.ForeignKey('p1.User',related_name='AccountStatus') 	##账号ID
	AccountStatus = models.IntegerField(default=0) #账号状态
	NameAuthStatus = models.IntegerField(default=0) #实名认证状态
	ContactStatus = models.IntegerField(default=0) #通讯录审核状态
	CarrierAuthStatus = models.IntegerField(default=0) #运营商认证状态
	DeviceAuthStatus = models.IntegerField(default=0) #设备验证状态
	BankCardAuthStatus = models.IntegerField(default=0) #银行卡绑定状态


	class Meta:
        	db_table = 'AccountStatus'


class AccountInfo(models.Model):	
	account = models.ForeignKey('p1.User',related_name='AccountInfo') 	##账号ID
	ProfileImgURL = models.URLField()	#账号头像
	NickName = models.CharField(max_length=5)	#账号昵称
	PhoneNumber = models.IntegerField()	#手机号
	CarrierCode = models.IntegerField(default=0)	#运营商代码
	InviterID = models.IntegerField()	#邀请人ID
	Address	= models.CharField(max_length=30) #地址
	Mail = models.EmailField() #邮箱

	class Meta:
		db_table = 'AccountInfo'

class Devices(models.Model):
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


	class Meta:
		db_table = 'Devices'
