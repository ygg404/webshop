# -*-coding:utf-8-*-
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views  # new

urlpatterns += [
	url(r'^learn/ajax_demo/$', learn_views.ajax_demo),
]