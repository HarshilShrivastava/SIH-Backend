from django.db import models
from Candidate.models import(
    SocialMediaTags,
    SocioeconomicTags
)
from django.core.validators import MaxValueValidator,MinValueValidator
from quiz.models import Domain
# Create your models here.
class Blogs(models.Model):
    Title=models.CharField(max_length=255)
    Description=models.TextField()
    photo=models.ImageField(upload_to="blogs")
    Refrences=models.URLField(max_length = 255)
    Added=models.DateTimeField(auto_now_add=True)
    Rating = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(5)],blank=True,null=True,default=0)
    Apply=models.URLField(max_length=255)
    Domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    SocialMediaTags=models.ManyToManyField(SocialMediaTags,blank=True)# only
    SocioeconomicTags=models.ManyToManyField(SocioeconomicTags,blank=True)



class Courses(models.Model):
    Title=models.CharField(max_length=255)
    Description=models.TextField()
    By=models.CharField(max_length=255)
    photo=models.ImageField(upload_to="courses")
    Refrences=models.URLField(max_length = 255)
    Rating = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(5)],blank=True,null=True,default=0)
    Apply=models.URLField(max_length=255)
    Added=models.DateTimeField(auto_now_add=True)
    Domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    SocialMediaTags=models.ManyToManyField(SocialMediaTags,blank=True)
    SocioeconomicTags=models.ManyToManyField(SocioeconomicTags,blank=True)


class Scheme(models.Model):
    Title=models.CharField(max_length=255)
    Description=models.TextField()
    By=models.CharField(max_length=255)
    photo=models.ImageField(upload_to="courses")
    Refrences=models.URLField(max_length = 255)
    Added=models.DateTimeField(auto_now_add=True)
    Apply=models.URLField(max_length=255)
    Domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    Rating = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(5)],blank=True,null=True,default=0)
    SocialMediaTags=models.ManyToManyField(SocialMediaTags,blank=True)
    SocioeconomicTags=models.ManyToManyField(SocioeconomicTags,blank=True)