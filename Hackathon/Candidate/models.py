from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Recruit(models.Model):
    User=models.OneToOneField(User , on_delete=models.CASCADE)
    Name=models.CharField( max_length=50)
    Address=models.CharField( max_length=250)
    Resume=models.FileField( upload_to="media", max_length=100)


class Skill(models.Model):
    fromRecruit=models.OneToOneField(Recruit, on_delete=models.CASCADE)
    Skill1=models.CharField( max_length=50,null=True)
    Skill2=models.CharField( max_length=50,null=True)
    Skill3=models.CharField( max_length=50,null=True)
    Skill4=models.CharField( max_length=50,null=True)


class MCQresult(models.Model):
    from_Recruit=models.OneToOneField(Recruit, on_delete=models.CASCADE)
    Skill1=models.CharField( max_length=50,null=True)
    Skill2=models.CharField( max_length=50,null=True)
    Skill3=models.CharField( max_length=50,null=True)
    Skill4=models.CharField( max_length=50,null=True)    