#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests,json,time,sys
from server_zoo import GetJob



def login(data_url):
        data={"username":"xiaoshuo","password": '123qwe!'}
        x=requests.session()
        url="http://192.168.137.1:8000/api-auth/login/"
        result1 = x.get(url)
        csrfToken = result1.cookies['csrftoken']
        data={"username":"xiaoshuo","password": '123qwe!','csrfmiddlewaretoken': csrfToken,}
        result = x.post(url,data=data)
        #print result.text
        req = x.get(data_url)
        return req.text






def create(data_url):
	create_log = {}
	result = login(data_url)
	b = json.loads(result)
	for i in  b['data']:
		result = login(data_url)
		b = json.loads(result)
		a=GetJob()
		nowtime=time.strftime('%Y-%m-%d_%H')
		path=task_dir +  i['hid'] 
		result = a.create(path,nowtime,False)
		create_log[path] = result
	return create_log


def get(product_id):
	data_url = 'http://192.168.137.1:8000/api/v1/Product_Server/id/%s/'%product_id
	task_dir='/task/%s/'%product_id
	a=GetJob()
	result = a.get_children(task_dir) 
	return  result


if __name__=="__main__" or len(sys.argv) == 3:  
	if len(sys.argv) == 3:
		product_id = sys.argv[2]
		if  sys.argv[1] == 'put':
			result = create(data_url)
			print result
	if  sys.argv[1] == 'delete' and len(sys.argv) == 4:
		a=GetJob()
		product_id = sys.argv[2]
		hid=sys.argv[3]
		result = a.delete('/task/%s/%s'%(product_id,hid))
		print  result

		
		
