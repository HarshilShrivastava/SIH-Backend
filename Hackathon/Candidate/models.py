from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator,MinValueValidator
from quiz.models import(
    Domain,
    SubDomain
)
from Organization.models import (
    Jobs
)
User = get_user_model()


class SocialMedia(models.Model):
    name=models.CharField( max_length=50,null=True)
    def __str__(self):
        return self.name
 
class SocialMediaTags(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
        return self.name

class SocioeconomicTags(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
        return self.name

class Residence(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Skills(models.Model):
    Name=models.CharField(max_length=200)

class Recruit(models.Model):
    User=models.OneToOneField(User , on_delete=models.CASCADE)
    Name=models.CharField( max_length=50)
    Address=models.CharField( max_length=250)
    TechRating = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10)],blank=True,null=True,default=0)
    MarketRating = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10)],blank=True,null=True,default=0)
    AttemptTech=models.PositiveIntegerField(null=True,blank=True,default=0)
    AttemptMarket=models.PositiveIntegerField(null=True,blank=True,default=0)
    Resume=models.FileField( upload_to="media", max_length=100)
    Socialmedia = models.ManyToManyField(SocialMedia, blank=True)
    Time=models.FloatField(blank=True,null=True,default=0)
    Familyincome=models.PositiveIntegerField(null=True,blank=True,default=0)
    Residence=models.ForeignKey(Residence,on_delete=models.CASCADE,null=True)
    SocialMediaTags=models.ManyToManyField(SocialMediaTags,blank=True)
    SocioeconomicTags=models.ManyToManyField(SocioeconomicTags,blank=True)
    Experience=models.FloatField()
    Bio=models.TextField()
    Skills=models.ManyToManyField(Skills,blank=True)


class Certificate(models.Model):
    Recruit=models.ForeignKey(Recruit,on_delete=models.CASCADE)
    Name=models.CharField(max_length=255)
    File=models.FileField( upload_to="certificate/")

    
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


class FulllistMarks(models.Model):
    Recruit=models.ForeignKey(Recruit , on_delete=models.CASCADE)
    Roundone = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10)],blank=True,null=True,default=0)
    RoundTwo1 = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10)],blank=True,null=True,default=0)
    RoundTwo2 = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10)],blank=True,null=True,default=0)
    RoundThree1 = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10)],blank=True,null=True,default=0)
    RoundThree2 = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10)],blank=True,null=True,default=0)
    TimeStamp=models.DateTimeField(auto_now_add=True)
