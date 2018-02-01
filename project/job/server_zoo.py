#!/usr/bin/python
# -*- coding:utf-8 -*-
import time,sys,os,json,threading,redis
import logging,ConfigParser,subprocess
from kazoo.client import KazooClient,KazooState
from optparse import OptionParser
from hashlib import md5


os.environ["TZ"] = "Asia/Shanghai"
zk_host='192.168.137.129:2181'




logging.basicConfig()
class Logger:
    def __init__(self,logname,logfile,loglevel):
        self.__logger = logging.getLogger(logname)
        fhandler = logging.FileHandler(logfile)
        chandler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fhandler.setFormatter(formatter)
        chandler.setFormatter(formatter)
        self.__logger.addHandler(fhandler)
        self.__logger.addHandler(chandler)
        if loglevel == "DEBUG":
            fhandler.setLevel(logging.DEBUG)
            chandler.setLevel(logging.DEBUG)
            self.__logger.setLevel(logging.DEBUG)
        else:
            fhandler.setLevel(logging.INFO)
            chandler.setLevel(logging.INFO)
            self.__logger.setLevel(logging.INFO)
    def debug(self,msg):
        self.__logger.debug(msg)
    def info(self,msg):
        self.__logger.info(msg)
    def error(self,msg):
        self.__logger.error(msg)

log_handler = Logger('zoo','./zoo.log','DEBUG')

class GetJob:
	def __init__(self):
		self.zk = KazooClient(hosts=zk_host)
		self.zk.start()
		log_handler.info('link to zkserver  %s success'%zk_host)


	def check(self,path):
		try:
			result =  self.zk.exists(path)
			return result
		except:
			log_handler.error('zk check exits %s error'%path)

	def get(self,path):
		try:
			result = self.zk.get(path)
			return result
		except:
			log_handler.error('zk get path  %s error'%path)

	def get_children(self,path):
		try:
                        result = self.zk.get_children(path,None)
                        return result
                except:
                        log_handler.error('zk get children path  %s error'%path)

	def create(self,path,info,tag):
		try:
			result = self.zk.create(path,info,ephemeral = tag)
			return result
		except:
			log_handler.error('zk create path  %s error'%path)
	
	def delete(self,path):
		try:
                        result = self.zk.delete(path)
                        return result
                except:
                        log_handler.error('zk delete path  %s error'%path)

	def init_key(self,server_key):
		result =  self.check(agent_root)
		if not result:
			log_handler.info('client key not exits %s  result %s'%(server_key,result))	
		else:
			result = self.get(agent_root)
			key_ip = result[0].split('_')[0]
			print key_ip,server_ip
                	if key_ip != server_ip:
				log_handler.error('client key other ip  %s  exits %s  result %s'%(key_ip,server_key))	
				sys.exit(9)
		result = self.create(agent_root,'%s_%s'%(server_ip,version),True)
		print result

	
	def watch_path(self,path,funt):
		self.zk.ChildrenWatch(agent_root,funt)
	
