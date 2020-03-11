from django.db import models
from Organization.models import Jobs
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
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


class Application(models.Model):
    by_university=models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="university")
    proposal_text=models.TextField()
    at=models.DateTimeField(  auto_now_add=True)
    apply_on=models.ForeignKey(Jobs, on_delete=models.CASCADE,related_name="job")
    