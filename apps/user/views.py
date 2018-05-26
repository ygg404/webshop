#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json
from apps.user.models import *

# Create your views here.
def register(request):
	return render(request, 'register.html')
	
def register_handle(request):
	post = request.POST
	uname = post.get('user_name')
	upwd  = post.get('pwd')
	cpwd  = post.get('cpwd')
	uemail  = post.get('email')
	
	user = UserInfo()
	user.uname = uname
	user.upwd  = upwd
	user.uemail = uemail
	
	try:
		UserInfo.objects.get(uname=uname)
	except :
		user.save()
		return render(request,  'error.html')
	#return render(request, "login.html")
	return HttpResponseRedirect("/user/register")

def login(request):
	return  render(request,'ulogin.html')

def login_handle(request):
	post = request.POST
	uname = post.get('user_name')
	upwd  = post.get('pwd')
	resp = {'errorcode': 100, 'detail': 'Get success'}
	return HttpResponse(json.dumps(resp), content_type="application/json")