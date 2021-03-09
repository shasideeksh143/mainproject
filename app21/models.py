from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    contactno=models.IntegerField(unique=True)
    username=models.CharField(max_length=20,unique=True)
class LoginModel(models.Model):
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=15)


