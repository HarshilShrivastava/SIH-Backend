from django.db import models
# from Candidate.models import Recruit
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
    Question_text=models.TextField()
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
    

class DomainQuestion(models.Model):
    Question_text=models.TextField()
    Domain=models.ForeignKey(Domain,on_delete=models.CASCADE,related_name="domain_specific")
    SubDomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.Question_text
    

# class DomainMarks(models.Model):
#     Total=models.PositiveIntegerField(null=True)
#     Domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
#    # Recruit2=models.ForeignKey(cm.Recruit,on_delete=models.CASCADE,related_name="candidate_profile")


# class SubDomainMarks(models.Model):
#     Total=models.PositiveIntegerField(null=True)
#     SubDomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE)
#     #Recruit3=models.ForeignKey(Recruit,on_delete=models.CASCADE,related_name="candidate profile")


class DomainAnswer(models.Model):
    Question_related_to=models.ForeignKey(DomainQuestion,on_delete=models.CASCADE,related_name="Question_domain") 
    from_Domain=models.ForeignKey(Domain,on_delete=models.CASCADE,related_name="from_domain_in_specific")
    SubDomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE,null=True,blank=True)
    Weightage=models.PositiveIntegerField() 
    Answer_text=models.TextField()
    def __str__(self):
        return self.Answer_text    