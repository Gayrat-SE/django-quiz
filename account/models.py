from django.db import models

# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     phone_number = models.CharField(max_length=13, blank=True, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13)