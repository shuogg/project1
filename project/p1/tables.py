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


class Product(models.Model):
	product_id = models.IntegerField(unique=True,primary_key=True)  #产品ID
	product_name = models.CharField(max_length=30)    #设备名称
	owner = models.ForeignKey('p1.User',related_name='Product')  #用户
	create_time = models.DateField(auto_now_add=True)      #建立时间
	class Meta:
		db_table = 'Product'


class Native_Host(models.Model):
	idc_name = models.CharField(unique=True,primary_key=True,max_length=16)  #机房名
	lan_ip = models.CharField(max_length=16,null = True)  #内网ip地址
	wan_ip = models.CharField(max_length=16,null = True)  #外网ip地址
	hid = models.CharField(max_length=30,null=True)          #机器hid
	Cabinet = models.CharField(max_length=30,null=True)          #机柜
	type =  models.CharField(max_length=16,null = True) #机器类型
	cpu_type = models.CharField(max_length=30,null = True)    #CPU类型
	cpu_number  = models.IntegerField(null=True) #CPU核心数量
	memory_size = models.CharField(max_length=20,null = True)    #内存大小
	disk_size = models.CharField(max_length=20,null = True)    #硬盘大小
	disk_type= models.CharField(max_length=20,null = True)    #硬盘类型
	create_time = models.DateField() 	#上架日期  


	class Meta:
		db_table = 'Native_Host'

class Idc_Host(models.Model):
	idc_name = models.CharField(unique=True,primary_key=True,max_length=16)  #机房名 #云名称
	lan_ip = models.CharField(max_length=16,null = True)  #内网ip地址
	wan_ip = models.CharField(max_length=16,null = True)  #外网ip地址
	hid = models.CharField(max_length=30,null=True)          #机器hid
	type =  models.CharField(max_length=16,null = True) #机器类型
	cpu_type = models.CharField(max_length=30,null = True)    #CPU类型
	cpu_number  = models.IntegerField(null=True) #CPU核心数量
	memory_size = models.CharField(max_length=20,null = True)    #内存大小
	disk_size = models.CharField(max_length=20,null = True)    #硬盘大小
	disk_type= models.CharField(max_length=20,null = True)    #硬盘类型
	create_time = models.DateField() 	#上架日期  


	class Meta:
		db_table = 'Idc_Host'


class Product_Host(models.Model):
	product_id = models.IntegerField(null = False)  #产品ID
	product_name = models.CharField(max_length=16,null = True) #产品名称
	lan_ip = models.CharField(max_length=16,null = True)  #内网ip地址
	wan_ip = models.CharField(max_length=16,null = True)  #外网ip地址
	hid = models.CharField(max_length=30,primary_key=True)          #机器hid
	type =  models.CharField(max_length=16,null=True) #机器类型
	cpu_type = models.CharField(max_length=30,null = True)    #CPU类型
	cpu_number  = models.IntegerField(null=True) #CPU核心数量
	memory_size = models.CharField(max_length=20,null = True)    #内存大小
	disk_size = models.CharField(max_length=20,null = True)    #硬盘大小
	disk_type= models.CharField(max_length=20,null = True)    #硬盘类型
	create_time = models.DateField() 	#上架日期  
	native_host =  models.CharField(max_length=30,null=True) #物理机ip

	def __unicode__(self):
		return self.hid

	class Meta:
		db_table = 'Product_Host'


class Product_Server(models.Model):
	server_id = models.CharField(max_length=16,null = False,primary_key=True)  #区组ID
	server_name = models.CharField(max_length=16,null = True) #区组名称
	server_type = models.CharField(max_length=16,null = True)  #区组类型
	server_ip =  models.CharField(max_length=30,null=True) #区组ip
	product_id = models.IntegerField(null = False)
	product_name = models.CharField(max_length=16,null = True)  #区组对应的产品
	hid = models.CharField(max_length=30)          #机器hid
	open_time = models.DateField() #开服时间
	created_at = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.server_id

	class Meta:
		db_table = 'Product_Server'




class Product_Agent(models.Model):
	product_id = models.IntegerField(null = False)  #产品ID
	product_name = models.CharField(max_length=16,null = True) #产品名称
	hid = models.CharField(max_length=30,primary_key=True)          #机器hid
	agentname =  models.CharField(max_length=40,null=True) #agent name
	status = models.IntegerField(default=0)    #是否在线
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.hid

	class Meta:
		db_table = 'Product_Agent'



class Product_cmd(models.Model):
	product_id = models.IntegerField(null = False)  #产品ID
	product_name = models.CharField(max_length=16,null = True) #产品名称
	cmd_name = models.CharField(max_length=16,null = True)  #内网ip地址
	cmd_type = models.CharField(max_length=16,null = True)
	owner = models.CharField(max_length=16,null = True)  #外网ip地址
	last_time = models.DateField() 

	def __unicode__(self):
		return self.cmd_name

	class Meta:
		db_table = 'Product_cmd'
