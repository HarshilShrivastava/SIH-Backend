from django.db import models
from Candidate.models import(
    SocialMediaTags,
    SocioeconomicTags
)
# Create your models here.
class Blogs(models.Model):
    Title=models.CharField(max_length=255)
    Description=models.TextField()
    photo=models.ImageField(upload_to="blogs")
    Refrences=models.URLField(max_length = 255)
    Apply=models.URLField(max_length=255)
    SocialMediaTags=models.ManyToManyField(SocialMediaTags,blank=True)
    SocioeconomicTags=models.ManyToManyField(SocioeconomicTags,blank=True)



class Courses(models.Model):
    Title=models.CharField(max_length=255)
    Description=models.TextField()
    By=models.CharField(max_length=255)
    photo=models.ImageField(upload_to="courses")
    Refrences=models.URLField(max_length = 255)
    Apply=models.URLField(max_length=255)
    SocialMediaTags=models.ManyToManyField(SocialMediaTags,blank=True)
    SocioeconomicTags=models.ManyToManyField(SocioeconomicTags,blank=True)