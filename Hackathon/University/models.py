from django.db import models
from django.contrib.auth import get_user_model
from Organization.models import (
    Jobs
)
User = get_user_model()


class Profile(models.Model):
    User=models.OneToOneField(User,  on_delete=models.CASCADE)
    Name=models.CharField( max_length=250)
    Address=models.TextField()
    Website=models.URLField( max_length=200)
    Conteact_no=models.CharField( max_length=50)
    Type=models.CharField( max_length=50)
    University=models.CharField( max_length=50)
    AICTE_college_code=models.CharField( max_length=50)
    Email=models.EmailField( max_length=254)


class Jobenquiry(models.Model):
    University=models.ForeignKey(Profile , on_delete=models.CASCADE)
    At=models.DateTimeField(  auto_now_add=True)
    proposal=models.TextField()
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)