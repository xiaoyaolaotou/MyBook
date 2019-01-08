#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/27 0027 下午 3:10
__Author__ = '村长'

import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    import django
    django.setup()

    from app01 import models

    # ret = models.Person.objects.filter(id__gt=1,id__lt=4)
    # print(ret)
    #
    # ret = models.Person.objects.filter(id__in=[7,1,3])
    # print(ret)

    # 正向查找--外键的查询操作

    book_obj = models.Book.objects.all().first()
    ret = book_obj.publisher
    # print(ret)


    ret = models.Book.objects.filter(id=9).values('publisher__name')
    # print(ret)


    ###反向查询

    #1.基于对象查询
    # publisher_obj = models.Publisher.objects.filter(id=4).first()
    # print(publisher_obj)
    # ret = publisher_obj.book_set.all()
    # ret = publisher_obj.books.all()
    # print(ret)


    ### 2.基于双下划线查询
    # ret = models.Publisher.objects.filter(id=9).values_list('book__title')
    # print(ret)



    ### 多对多关联
    # 1.create
    # auther_obj  = models.Author.objects.filter(id=6).first()
    # print(auther_obj)

    # ret = auther_obj.book.all()
    # print(ret)
    # auther_obj.book.create(title='金瓶梅',publisher_id=4)


    #add
    # book_objs = models.Book.objects.filter(id=9)
    # print(book_objs)


    # auther_objs = models.Author.objects.filter(id=6).first()
    # auther_objs.book.clear()
    # print(auther_objs)


    #聚合
    # from django.db.models import Avg,Sum,Max
    # ret = models.Book.objects.all().aggregate(Avg('price'),Sum('price'),Max('price'))
    # print(ret)

    # F和Q
    from django.db.models import F,Q
    # ret = models.Book.objects.filter(price__gt=9.99)
    # print(ret)
    # ret = models.Book.objects.filter(kucun__gt=F("maichu"))
    # print(ret)

    # obj = models.Book.objects.first()
    # obj_xx = obj.maichu
    # print(obj_xx)
    #
    # models.Book.objects.filter(id=9).update(kucun=F("kucun")*3)


    #### 一对一查询
    # author = models.Author.objects.filter(id=8).first()
    # obj = author.detail
    # print(obj.hobby)
    # print(obj.addr)


    # ret = models.Book.objects.filter(title__contains='li')
    # print(ret)
    #
    #
    # ret = models.Book.objects.filter(id=10).values_list("publisher__name")
    # print(ret.distinct())

    from app01 import models

    # ret = models.Publisher.objects.create()

    #批量创建
    # ret = [models.Publisher(name="北京出版社{}".format(i)) for i in range(100)]
    # models.Publisher.objects.bulk_create(ret,10)
    #







# i = 10
# while i<=10:
#     if i ==10:
#         print(i)
#         break

# while True:
#     for i in range(1,11):
#         if i ==7:
#             continue
#         print(i)
#     break



from subprocess import PIPE,Popen
import os
import sys
OLD = "http://1.1.1.1/"
NEW = "http://1.1.1.1/"
GROUP = "cloudzone"
addr = "/root/git"

def clone():
    print("clone代码")
    with open('gitwa','r')as f:
        for line in f:
            proc = Popen('git clone {0}{1}/{2}'.format(OLD,GROUP,line),shell=True,stdout=PIPE,stdin=PIPE)
            txt = proc.stdout.read()
            res = proc.wait()
            print(txt,res)

def modify():
    print("修改代码地址")
    with open('gitwa','r') as f:
        for line in f:
            strs = line.split('.')[0]
            print(strs)
            os.chdir("{0}/{1}".format(addr,strs))
            print(os.getcwd())
            proc = Popen('git remote set-url origin {0}{1}/{2}'.format(NEW,GROUP,line),shell=True,stdout=PIPE,stdin=PIPE)
            if proc.wait() == 0:
                print(proc.stdout.read())
            else:
                print("error")
                sys.exit(1)

def push():
    print("推送代码到远程仓库")
    with open('gitwa','r') as f:
        for line in f.readlines():
            strs = line.split('.')[0]
            os.chdir("{0}/{1}".format(addr,strs))
            os.system("git add .")
            os.system("git remote add origin {0}{1}/{2}".format(NEW,GROUP,strs))
            os.system("git add .")
            os.system('git commit -m "Initial commit"')
            os.system('git push -u origin master')

if __name__ == '__main__':
    # clone()
    # modify()
    # push()
    pass


import json
s = {'name':'list'}
st = json.dumps(s)
print(st,type(st))

s = '\t'
print(len(s))


























