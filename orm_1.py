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
    publisher_obj = models.Publisher.objects.filter(id=4).first()
    # print(publisher_obj)
    ret = publisher_obj.book_set.all()
    # ret = publisher_obj.books.all()
    # print(ret)


    ### 2.基于双下划线查询
    # ret = models.Publisher.objects.filter(id=9).values_list('book__title')
    # print(ret)



    ### 多对多关联
    # 1.create
    auther_obj  = models.Author.objects.filter(id=6).first()
    # print(auther_obj)

    ret = auther_obj.book.all()
    # print(ret)
    # auther_obj.book.create(title='金瓶梅',publisher_id=4)


    #add
    book_objs = models.Book.objects.filter(id=9)
    # print(book_objs)


    auther_objs = models.Author.objects.filter(id=6).first()
    auther_objs.book.clear()
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






























