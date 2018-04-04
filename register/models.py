from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    gender = models.IntegerField(default=1)
    phone = models.IntegerField
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    head_pic = models.CharField(max_length=255,default=0)
    attr = models.IntegerField(default=0)
    authority = models.IntegerField(default=0)
    display = models.IntegerField(default=0)