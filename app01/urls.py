#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/20 0020 上午 11:08
__Author__ = '村长'

from django.urls import path,re_path
from app01 import views

urlpatterns = [
    re_path(r'^book_list/$',views.book_list,name='book_list'),

]