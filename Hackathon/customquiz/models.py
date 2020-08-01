from django.db import models
from Organization.models import Company
import uuid

class Domain(models.Model):
    Name=   models.CharField(max_length=255)
    def __str__(self):
        return self.Name
    
class SubDomain(models.Model):
    Name= models.CharField(max_length=255)
    From = models.ForeignKey(Domain, on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
    

class Question(models.Model):
    Organization=models.ForeignKey(Company,on_delete=models.CASCADE)
    key=models.IntegerField()
    Question_text=models.TextField()
    Domain=models.ForeignKey(Domain,on_delete=models.CASCADE,related_name="domain")
   

class Answer(models.Model):
    Question_related_to=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="Question") 
    Weightage=models.PositiveIntegerField() 
    Answer_text=models.TextField()
    def __str__(self):
        return self.Answer_text
    
