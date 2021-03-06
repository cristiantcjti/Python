from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.

class Patient(models.Model):
    id_handbook = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, null=False)
    rg = models.CharField(max_length=9)
    ufrg = models.CharField(max_length=3)
    email = models.CharField(max_length=30)
    cellphone = models.CharField(max_length=11)
    telephone = models.CharField(max_length=10)
    medical_insurance = models.CharField(max_length=70)
    card_number = models.IntegerField()
    card_validity = models.CharField(max_length=5)
    contact_way = models.CharField(null=True, max_length=9)
    newsletter = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id_handbook)
    
    class Meta:
        verbose_name = "Register"
        verbose_name_plural = "Registers"

class Insurance(models.Model):
    id_insurance = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=70)

    def __str__(self):
        return str(self.id_insurance)
    
    class Meta:
        verbose_name = "Medical_Insurance"
        verbose_name_plural = "Medical_Insurance"