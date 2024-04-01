from django.db import models


# Create your models here.
class Parent1(models.Model):
    f1 = models.CharField(max_length=30)
    f2 = models.CharField(max_length=30)

class Parent2(models.Model):
    f3 = models.CharField(max_length=30,primary_key=True)
    f4 = models.CharField(max_length=30)

class Child(Parent1,Parent2):
    f5 = models.CharField(max_length=30)
    f6 = models.CharField(max_length=30)

