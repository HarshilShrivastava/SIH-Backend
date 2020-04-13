from rest_framework import serializers
from .models import Company,Jobs
class companyserializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=["Name","Address","Email","City","State","Registration_no","website"]
class jobserializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields=['job_title','Job_Descreption','fields','Level','Minimum_experience','prefered_city','id']


class jobReadserializer(serializers.ModelSerializer):
    Name=serializers.SerializerMethodField('get_name')

    class Meta:
        model=Jobs
        fields=['job_title','Job_Descreption','fields','Level','Minimum_experience','prefered_city','id','Name']

    def get_name(self,info):
        data=info.by.Name
        return data