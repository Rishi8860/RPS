from distutils.command.upload import upload
from email.message import Message
from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class field(models.Model):
    Field=models.CharField(max_length=256,unique=True)
    About=models.CharField(max_length=256)
    def __str__(self):
        return self.Field
class Doctor(models.Model):
    CHOICE=(('Allergists/Immunologists','Allergists/Immunologists'),('Anesthesiologists','Anesthesiologists'),('Cardiologists','Cardiologists'),('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),('Critical Care Medicine Specialists','Critical Care Medicine Specialists'),('Dermatologists','Dermatologists'),('Endocrinologists','Endocrinologists'),('Emergency Medicine Specialists','Emergency Medicine Specialists'),('Family Physicians','Family Physicians'),('Gastroenterologists','Gastroenterologists'),('Geriatric Medicine Specialists','Geriatric Medicine Specialists'),('Hematologists','Hematologists'),('Hospice and Palliative Medicine Specialists','Hospice and Palliative Medicine Specialists'),('Infectious Disease Specialists','Infectious Disease Specialists'),('Internists','Internists'),('Medical Geneticists','Medical Geneticists'),('Nephrologists','Nephrologists'),('Obstetricians and Gynecologists','Obstetricians and Gynecologists'),('Oncologists','Oncologists'),('Ophthalmologists','Ophthalmologists'))
    ID=models.AutoField(primary_key=True,)
    Name=models.CharField(max_length=256)
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
class Facilities_no(models.Model):
    Beds=models.IntegerField()
    ICU_Beds=models.IntegerField()
    Ventilator=models.IntegerField()
    Equipments=models.IntegerField()
    Nurses=models.IntegerField()
    Staff=models.IntegerField()




