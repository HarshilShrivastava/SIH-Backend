from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from quiz.models import Domain,SubDomain


class SkillForJobs(models.Model):
    Name=models.CharField(max_length=200,primary_key=True,unique=True)
    def __str__(self):
        return self.Name
# Create your models here.
class Company(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Registration_no=models.CharField(max_length=50)
    website=models.URLField( max_length=200)


class Jobs(models.Model):
    by=models.ForeignKey(Company,  on_delete=models.CASCADE)
    job_title=models.CharField( max_length=50)
    Job_Descreption=models.TextField()
    Job_preprocess=models.TextField(null=True,blank=True)
    fields=models.ForeignKey(Domain, on_delete=models.CASCADE)
    Level=models.IntegerField()
    Minimum_experience=models.IntegerField()
    prefered_city=models.CharField( max_length=50)
    SubDomain=models.ManyToManyField(SubDomain)
    SkillRequired=models.ManyToManyField(SkillForJobs,blank=True)
    def __str__(self):
        return str(self.id)
    
