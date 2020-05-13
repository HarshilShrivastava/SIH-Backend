from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from quiz.models import(
    Domain,
    SubDomain
)
from Organization.models import (
    Jobs
)
User = get_user_model()

class Recruit(models.Model):
    User=models.OneToOneField(User , on_delete=models.CASCADE)
    Name=models.CharField( max_length=50)
    Address=models.CharField( max_length=250)
    TechRating = models.PositiveIntegerField( validators=[MaxValueValidator(10)],null=True,blank=True,default=0)
    MarketRating = models.PositiveIntegerField( validators=[MaxValueValidator(10)],null=True,blank=True,default=0)
    AttemptTech=models.PositiveIntegerField(null=True,blank=True,default=0)
    AttemptMarket=models.PositiveIntegerField(null=True,blank=True,default=0)
    Resume=models.FileField( upload_to="media", max_length=100)

class Skill(models.Model):
    fromRecruit=models.OneToOneField(Recruit, on_delete=models.CASCADE)
    Skill1=models.CharField( max_length=50,null=True)
    Skill2=models.CharField( max_length=50,null=True)
    Skill3=models.CharField( max_length=50,null=True)
    Skill4=models.CharField( max_length=50,null=True)


class GeneralMark(models.Model):
    Technology=models.PositiveIntegerField(null=True)
    Marketing=models.PositiveIntegerField(null=True)  
    Total=models.PositiveIntegerField(null=True)
    Recruit1=models.ForeignKey(Recruit,on_delete=models.CASCADE,related_name="candidate_view",null=True,blank=True)

class DomainMark(models.Model):
    Total=models.PositiveIntegerField(null=True)
    Domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    Recruit2=models.ForeignKey(Recruit,on_delete=models.CASCADE,related_name="candidate_profile",null=True,blank=True)


class SubDomainMark(models.Model):
    Total=models.PositiveIntegerField(null=True)
    SubDomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE)
    Recruit3=models.ForeignKey(Recruit,on_delete=models.CASCADE,related_name="candidate",null=True,blank=True)


class JobenquiryC(models.Model):
    Recruit=models.ForeignKey(Recruit , on_delete=models.CASCADE)
    At=models.DateTimeField( auto_now_add=True)
    proposal=models.TextField()
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)