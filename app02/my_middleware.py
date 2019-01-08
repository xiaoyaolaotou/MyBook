#! /usr/bin/env python
# encoding: utf-8
# @Time :2019/1/7 0007 下午 4:55
__Author__ = '村长'
"""
自定义中间件
"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

URL = ["/oo/","/app02/index/","/app02/reg/","/app02/person/"]

class ZiDingYi(MiddlewareMixin):
    def process_request(self,request):
        # print(request.path_info)
        # print(request.get_full_path())
        print("这是第一个中间件")
        # if request.path_info in URL:
        #     return redirect("/app02/person/")
        # else:
        #     return HttpResponse("滚")

    def process_response(self,request,response):
        print("这是一第一个中间件的response")
        # ret = HttpResponse("hahaha")
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        """
        :param request:  浏览器发来的请求对象
        :param view_func: 将要执行的视图函数名字
        :param view_args: 将要执行的视图函数位置参数
        :param view_kwargs: 将要执行的视图函数关键字参数
        :return:
        """
        print("这是第一个中间件的视图函数")
        print(view_func,type(view_func))
        return HttpResponse("process_view")


class MD2(MiddlewareMixin):
    def process_request(self,request):
        print("这是第二个中间件：MD2")

    def process_response(self,request,response):
        print("这是二第二个中间件的response")
        return response





