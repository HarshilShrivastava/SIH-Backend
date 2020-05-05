from django.db import models
from django.contrib.auth import get_user_model

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
    Question_text=models.TextField(max_length=100)
    Domain=models.ForeignKey(Domain,on_delete=models.CASCADE,related_name="domain")
    SubDomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.Question_text
    def __unicode__(self):
        return self.Question_text


class Answer(models.Model):
    Question_related_to=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="Question") 
    from_Domain=models.ForeignKey(Domain,on_delete=models.CASCADE,related_name="from_domain",null=True,blank=True)
    SubDomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE,null=True,blank=True)
    Weightage=models.PositiveIntegerField() 
    Answer_text=models.TextField()
    def __str__(self):
        return self.Answer_text
    
class GeneralMarks(models.Model):
    Technology=models.PositiveIntegerField(null=True)
    Marketing=models.PositiveIntegerField(null=True)  
    Total=models.PositiveIntegerField(null=True)
    Name=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="from_domain",null=True,blank=True)


class DomainQuestion(models.Model):
    Question_text=models.TextField()
    Domain=models.ForeignKey(Domain,on_delete=models.CASCADE,related_name="domain_specific")
    SubDomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.Question_text
    

class DomainMarks(models.Model):
    Total=models.PositiveIntegerField(null=True)
    Domain_final=models.CharField(max_length=25)
    Name_of_user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="for_final_marks",null=True,blank=True)



class DomainAnswer(models.Model):
    Question_related_to=models.ForeignKey(DomainQuestion,on_delete=models.CASCADE,related_name="Question_domain") 
    from_Domain=models.ForeignKey(Domain,on_delete=models.CASCADE,related_name="from_domain_in_specific")
    SubDomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE,null=True,blank=True)
    Weightage=models.PositiveIntegerField() 
    Answer_text=models.TextField()
    def __str__(self):
        return self.Answer_text    