from django.db import models


class Publisher(models.Model):
    """出版社"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128,null=False,unique=True)
    addr = models.CharField(max_length=128,null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """书"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,null=False,unique=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=99.99)
    kucun = models.IntegerField(default=1000)
    maichu = models.IntegerField(default=9)
    # publisher_id = models.ForeignKey(to="Publisher")
    publisher = models.ForeignKey(to="Publisher",on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title


class Author(models.Model):
    """作者表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,null=False,unique=True)
    book = models.ManyToManyField(to="Book")

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)
    birthday = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name







