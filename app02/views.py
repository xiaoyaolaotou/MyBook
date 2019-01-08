from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from app02 import models


def login(request):
    if request.method == "POST":
        user = request.POST.get("username", None)
        pwd = request.POST.get("password", None)
        if user == "lisi" and pwd == "123":
            return redirect("/author_list/")
        return redirect('/app02/login/')
    return render(request, "login.html")


def index(request):
    return render(request,'index.html')


def ajax_add(request):
    # print(request.GET)
    print(request.GET.get("i1"))
    print(request.GET.get("i2"))
    i1 = int(request.GET.get("i1"))
    i2 = int(request.GET.get("i2"))
    ret = i1 + i2
    return HttpResponse(ret)

def ajax_add_post(request):
    print(request.POST)
    i1 = int(request.POST.get("i1"))
    i2 = int(request.POST.get("i2"))

    ret = i1 + i2
    return HttpResponse(ret)

import json
from django.core import serializers
def person(request):
    ret = models.Person.objects.all()
    # person_list = []
    # for i in ret:
    #     person_list.append({'name':i.name,'age':i.age})
    # str = json.dumps(person_list)
    # print(str)
    # s = serializers.serialize("json",ret)
    # print(s)
    # print(type(s))
    # return HttpResponse(s)
    return render(request,'sweetalert_demo.html',{'person':ret})

def delete(request):
    code = {'code':0}
    del_id = request.GET.get("id")
    models.Person.objects.filter(id=del_id).delete()
    return JsonResponse(code)


def reg(request):
    form_obj = RegForm()
    if request.method == "POST":
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            #所有经过的校验数据都保存在cleaned_data
            print(form_obj.cleaned_data)
            models.UserInfo.objects.create(form_obj.cleaned_data)
    return render(request,'reg.html',{'form_obj':form_obj})


from django import forms

class RegForm(forms.Form):
    username = forms.CharField(max_length=16,
                           min_length=6,
                           error_messages={
                               "min_length":"不能少于6位",
                               "max_length":"不能大于16位",
                               "required":"不能为空"
                           },
                           required=True
                           )
    pwd = forms.CharField(max_length=16,
                          min_length=6,
                          error_messages={
                              "min_length": "不能少于6位",
                              "max_length": "不能大于16位",
                              "required": "不能为空"
                          },required=True
                          )
def index(request):
    print("这是app02的视图函数")
    return HttpResponse("middle")











