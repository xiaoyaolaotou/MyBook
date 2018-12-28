#! /usr/bin/env python
# encoding: utf-8
# @Time :2018/12/27 0027 下午 2:20
__Author__ = '村长'

import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    import django
    django.setup()

    from app01 import models

    ret = models.Person.objects.all()
    print(ret)

    ret = models.Person.objects.get(name='小黑')
    print(ret)
    # a = ret[0]
    # print(a.id)


    ret = models.Person.objects.filter(id__gt=2)
    print(ret)

    ret = models.Person.objects.values('id','name')
    print(ret)

    ret = models.Person.objects.values_list('name')
    print(ret)


    #单表查询之双下划线









