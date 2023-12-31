from django.contrib.auth.models import AbstractUser
from django.db import models




class CustomUser(AbstractUser):
    name = models.CharField(max_length=150,blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    street = models.CharField(max_length=150, blank=True)
    house_number = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=150, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True,blank=True)
    country = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True)
    tax_number = models.CharField(max_length=50, blank=True)
    bank_account = models.CharField(max_length=50, blank=True)
    invoices = models.ManyToManyField('reservation.Invoice', blank=True)

