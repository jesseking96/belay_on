from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone = models.CharField(max_length=200)
    emergency_contact_relationship=models.CharField(max_length=200)
    date_waiver_signed = models.DateField(auto_now=True)
