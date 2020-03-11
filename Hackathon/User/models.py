from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class user(AbstractUser):
    Is_Organization=models.BooleanField(null=True)
    Is_Candidate=models.BooleanField(null=True)
    Is_University=models.BooleanField(null=True)
    


    