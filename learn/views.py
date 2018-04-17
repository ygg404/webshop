# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import json 

def index(request):
    return render(request, 'login.html')
	

def ajax_demo(request):
	#print('ajax_demo')
    if request.method == 'POST':
        ret = {'status':False,'message':''}
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user,pwd)
        if user == '111' and pwd == '222':
            ret['status'] = True
            return HttpResponse(json.dumps(ret))
        else:
            ret['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps("222"))