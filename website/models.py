from distutils.command.upload import upload
from email.message import Message
from msilib.schema import Class
from operator import mod
from pyexpat import model
from typing_extensions import Required
from django.db import models

# Create your models here.
class field(models.Model):
    Field=models.CharField(max_length=256,unique=True)
    Field_Hindi=models.CharField(max_length=256,blank=True)
    About=models.CharField(max_length=256)
    def __str__(self):
        return self.Field
class Doctor(models.Model):
    ID=models.AutoField(primary_key=True,)
    Name=models.CharField(max_length=256)
    Name_Hindi=models.CharField(max_length=256,blank=True)
    Field=models.ForeignKey('field',on_delete=models.CASCADE)
    Photo=models.ImageField(upload_to='Doctors/')
    About=models.TextField()
    Joining=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Name

# Front Page slider data
class Slider(models.Model):
    Header=models.CharField(max_length=256,unique=True)
    Data=models.CharField(max_length=256,unique=True)
    def __str__(self):
        return self.Header
class Query(models.Model):
    Name=models.CharField(max_length=256)
    Contact=models.CharField(max_length=256)
    Sub=models.CharField(max_length=256)
    Email=models.CharField(max_length=256)
    Message=models.CharField(max_length=256)
    def __str__(self):
        return self.Name
class department(models.Model):
    Department=models.CharField(max_length=256,unique=True)
    Logo=models.ImageField(upload_to='Departments/')
    About=models.CharField(max_length=256)
    def __str__(self):
        return self.Department
# Carriers
class resume(models.Model): 
    Name=models.CharField(max_length=256)
    Contact=models.CharField(max_length=256)
    Department=models.CharField(max_length=256)
    Email=models.CharField(max_length=256)
    About_You=models.CharField(max_length=256)
    Resume=models.FileField(upload_to='Resume/')
    def __str__(self):
        return self.Name

# About
class about_u(models.Model):
    About_us=models.TextField()
    Front_page_photo=models.ImageField(upload_to='Front_page_photo/')
    def __str__(self) -> str:
        return self.About_us
class Know_Your_Founder(models.Model):
    Name=models.CharField(max_length=256,unique=True)
    Photo=models.ImageField(upload_to='Founder_photo/')
    About=models.TextField()




