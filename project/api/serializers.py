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






class ProductSerializer(serializers.Serializer):
	product_id = models.IntegerField(unique=True,primary_key=True)  #产品ID
	product_name = models.CharField(max_length=30)    #产品名称
	owner = models.ForeignKey('p1.User',related_name='Product')  #用户
	create_time = models.DateField()      #建立时间



	def create(self, validated_data):
		return Product.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.product_id = validated_data.get('product_id', instance.product_id )
		instance.product_name = validated_data.get('product_name', instance.product_name)
		instance.owner = validated_data.get('owner',instance.owner )
		instance.save()
		return instance

class ProductSerializer(serializers.ModelSerializer):
	#snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = Product
		fields = ('product_id', 'product_name','owner')
		#fields = ('name','username')


class Native_HostSerializer(serializers.Serializer):
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


	def create(self, validated_data):
		return Native_Host.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.idc_name = validated_data.get('idc_name', instance.idc_name)
		instance.lan_ip = validated_data.get('lan_ip', instance.lan_ip)
		instance.wan_ip = validated_data.get('wan_ip', instance.wan_ip)
		instance.hid = validated_data.get('hid', instance.hid)
		instance.Cabinet = validated_data.get('Cabinet', instance.Cabinet)
		instance.type = validated_data.get('type', instance.type)
		instance.cpu_type = validated_data.get('cpu_type', instance.cpu_type)
		instance.cpu_number = validated_data.get('cpu_number', instance.cpu_number)
		instance.memory_size = validated_data.get('memory_size', instance.memory_size)
		instance.disk_size = validated_data.get('disk_size', instance.disk_size)
		instance.disk_type = validated_data.get('disk_type', instance.disk_type)
		instance.create_time = validated_data.get('create_time', instance.create_time)
		instance.save()
		return instance

class Native_HostSerializer(serializers.ModelSerializer):
	#snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = Native_Host
		fields = ('idc_name','lan_ip','wan_ip','hid','Cabinet','type','cpu_type','cpu_number','memory_size','disk_size','disk_type','create_time')


		
class Idc_HostSerializer(serializers.Serializer):
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


	def create(self, validated_data):
		return Idc_Host.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.idc_name = validated_data.get('idc_name', instance.idc_name)
		instance.lan_ip = validated_data.get('lan_ip', instance.lan_ip)
		instance.wan_ip = validated_data.get('wan_ip', instance.wan_ip)
		instance.hid = validated_data.get('hid', instance.hid)
		instance.type = validated_data.get('type', instance.type)
		instance.cpu_type = validated_data.get('cpu_type', instance.cpu_type)
		instance.cpu_number = validated_data.get('cpu_number', instance.cpu_number)
		instance.memory_size = validated_data.get('memory_size', instance.memory_size)
		instance.disk_size = validated_data.get('disk_size', instance.disk_size)
		instance.disk_type = validated_data.get('disk_type', instance.disk_type)
		instance.create_time = validated_data.get('create_time', instance.create_time)
		instance.save()
		return instance

class Idc_HostSerializer(serializers.ModelSerializer):
	#snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = Idc_Host
		fields = ('idc_name','lan_ip','wan_ip','hid','type','cpu_type','cpu_number','memory_size','disk_size','disk_type','create_time')


class Product_HostSerializer(serializers.Serializer):
	product_id = models.IntegerField(null = False)  #机房名
	product_name = models.CharField(max_length=16,null = True) #产品名称
	lan_ip = models.CharField(max_length=16,null = True)  #内网ip地址
	wan_ip = models.CharField(max_length=16,null = True)  #外网ip地址
	hid = models.CharField(max_length=30,primary_key=True)          #机器hid
	type =  models.CharField(max_length=16,null = True) #机器类型
	cpu_type = models.CharField(max_length=30,null = True)    #CPU类型
	cpu_number  = models.IntegerField(null=True) #CPU核心数量
	memory_size = models.CharField(max_length=20,null = True)    #内存大小
	disk_size = models.CharField(max_length=20,null = True)    #硬盘大小
	disk_type= models.CharField(max_length=20,null = True)    #硬盘类型
	create_time = models.DateField()	#上架日期  
	native_host =  models.CharField(max_length=30,null=True) #物理机ip



	def create(self, validated_data):
		return Product_Host.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.product_name = validated_data.get('product_name',instance.product_name)
		instance.product_id = validated_data.get('product_id',instance.product_id)
		instance.hid = validated_data.get('hid',instance.hid)
		instance.lan_ip = validated_data.get('lan_ip', instance.lan_ip)
		instance.wan_ip = validated_data.get('wan_ip', instance.wan_ip)
		instance.create_time = validated_data.get('create_time', instance.create_time)
		instance.type = validated_data.get('type', instance.type)
		instance.cpu_type = validated_data.get('cpu_type', instance.cpu_type)
		instance.cpu_number = validated_data.get('cpu_number', instance.cpu_number)
		instance.memory_size = validated_data.get('memory_size', instance.memory_size)
		instance.disk_size = validated_data.get('disk_size', instance.disk_size)
		instance.disk_type = validated_data.get('disk_type', instance.disk_type)
		instance.native_host = validated_data.get('native_host', instance.native_host)
		instance.save()
		return instance

class Product_HostSerializer(serializers.ModelSerializer):
	#snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = Product_Host
		fields = ('product_id','product_name','lan_ip','wan_ip','hid','type','cpu_type','cpu_number','memory_size','disk_size','disk_type','create_time','native_host')




class  Product_ServerSerializer(serializers.Serializer):
	server_id = models.CharField(max_length=16,null = False)  #区组ID
	server_name = models.CharField(max_length=16,null = True) #区组名称
	server_type = models.CharField(max_length=16,null = True)  #区组类型
	server_ip =  models.CharField(max_length=30,null=True) #区组ip
	product_id = models.IntegerField(null = False)  #产品ID
	product_name = models.CharField(max_length=16,null = True)  #区组对应的产品
	hid = models.CharField(max_length=30,primary_key=True)          #机器hid
	open_time = models.DateTimeField() #开服时间


	def create(self, validated_data):
		return Product_Server.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.server_id = validated_data.get('server_id', instance.server_id)
		instance.server_name = validated_data.get('server_name',instance.server_name)
		instance.server_type = validated_data.get('server_type', instance.server_type)
		instance.server_ip = validated_data.get('server_ip', instance.server_ip)
		instance.product_id = validated_data.get('product_id', instance.product_id)
		instance.product_name = validated_data.get('product_name',instance.product_name)
		instance.hid = validated_data.get('hid', instance.hid)
		instance.open_time = validated_data.get('open_time', open_time)
		instance.save()
		return instance
		

class Product_ServerSerializer(serializers.ModelSerializer):
	#snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = Product_Server
		fields = ('server_id','server_name','server_type','product_name','server_ip','hid','open_time','product_id')



class Product_AgentSerializer(serializers.Serializer):
	product_id = models.IntegerField(null = False)  #产品ID
	product_name = models.CharField(max_length=16,null = True) #产品名称
	hid = models.CharField(max_length=40,primary_key=True)          #机器hid
	agentname =  models.CharField(max_length=30,null=True) #agent name
	status = models.IntegerField(default=0)    #是否在线


	def create(self, validated_data):
		return Product_Agent.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.product_id = validated_data.get('product_id', instance.product_id)
		instance.product_name = validated_data.get('product_name', instance.product_name)
		instance.hid = validated_data.get('hid', instance.hid)
		instance.agentname = validated_data.get('agentname', instance.agentname)
		instance.status = validated_data.get('status', instance.status)
		instance.save()
		return instance

class Product_AgentSerializer(serializers.ModelSerializer):
	#snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = Product_Agent
		fields = ('product_id','product_name','hid','agentname','status')




class Product_cmdSerializer(serializers.Serializer):
	product_id = models.IntegerField(null = False)  #产品ID
	product_name = models.CharField(max_length=16,null = True) #产品名称
	cmd_name = models.CharField(max_length=16,null = True)  #内网ip地址
	cmd_type = models.CharField(max_length=16,null = True)
	owner = models.CharField(max_length=16,null = True)  #外网ip地址
	last_time = models.DateField() 

	def create(self, validated_data):
		return Product_cmd.objects.create(**validated_data)
	def update(self, instance, validated_data):
		instance.product_id = validated_data.get('product_id', instance.product_id)
		instance.product_name = validated_data.get('product_name', instance.product_name)
		instance.cmd_name = validated_data.get('cmd_name', instance.cmd_name)
		instance.cmd_type = validated_data.get('cmd_type', instance.cmd_type)
		instance.owner = validated_data.get('owner', instance.owner)
		instance.last_time = validated_data.get('last_time', instance.last_time)
		instance.save()
		return instance

class Product_cmdSerializer(serializers.ModelSerializer):
	#snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	class Meta:
		model = Product_cmd
		fields = ('product_id','product_name','cmd_name','cmd_type','owner','last_time')

