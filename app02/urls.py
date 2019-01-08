#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/20 0020 下午 1:45
__Author__ = '村长'

from django.urls import path,re_path

from app02 import views

urlpatterns = [
    re_path(r'login/$',views.login,name='login'),
    re_path(r'index/$',views.index,name='index'),
    re_path(r'ajax_add/$',views.ajax_add,name='ajax_add'),
    re_path(r'ajax_add_post/$',views.ajax_add_post,name='ajax_add_post'),
    re_path(r'person/$',views.person,name='person'),
    re_path(r'delete/$',views.delete,name='delete'),
    re_path(r'reg/$',views.reg,name='reg'),
    re_path(r'index/$',views.index,name='index'),
]





