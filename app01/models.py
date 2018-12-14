from django.db import models


class Publisher(models.Model):
    """出版社"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128,null=False,unique=True)
    addr = models.CharField(max_length=128,null=True)


class Book(models.Model):
    """书"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,null=False,unique=True)
    # publisher_id = models.ForeignKey(to="Publisher")
    publisher = models.ForeignKey(to="Publisher",on_delete=models.DO_NOTHING,default=None)


class Author(models.Model):
    """作者表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,null=False,unique=True)
    book = models.ManyToManyField(to="Book")







