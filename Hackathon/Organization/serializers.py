from rest_framework import serializers
from .models import Company,Jobs,Application
class companyserializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=["Name","Address","Email","City","State","Registration_no","website"]
class jobserializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields=["job_title","Job_Descreption","Level","Minimum_experience","prefered_city","fields"]
        
class Jobapply(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields=["proposal_text"]

class jobapplication(serializers.ModelSerializer):

    class Meta:
        model=Application
        fields=["proposal_text","at"]