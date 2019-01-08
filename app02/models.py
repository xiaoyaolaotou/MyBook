from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Person(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    name = models.CharField(max_length=32,unique=True,null=True)
    pwd = models.CharField(max_length=32)

    def __str__(self):
        return self.name