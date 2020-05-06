from .models import Recruit,MCQresult,Skill,JobenquiryC
from rest_framework import serializers
class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recruit
        fields=["Name","Address","Resume"]
class RatingMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recruit
        fields=["MarketRating"]

class RatingTechSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recruit
        fields=["TechRating"]

class JobapplySerializer(serializers.ModelSerializer):
    class Meta:
        model=JobenquiryC
        fields=['proposal']
class ApplicationSerializer(serializers.ModelSerializer):
    Recruit_obj=serializers.SerializerMethodField('get_Recruit_name')
    Recruit_add_obj=serializers.SerializerMethodField('get_Recruit_address')

    Resume_obj=serializers.SerializerMethodField('get_Recruit_Resume')
    class Meta:
        model=JobenquiryC
        fields=['proposal','At','Recruit_obj','Resume_obj','Recruit_add_obj','Rating']
    def get_Recruit_name(self,info):
        data=info.Recruit.Name
        return data
    def get_Recruit_Resume(self,info):
        data=info.Recruit.Resume.url
        return data
    def get_Recruit_address(self,info):
        data=info.Recruit.Address
        return data

class ViewAppilicationSerializer(serializers.ModelSerializer):
    job_name=serializers.SerializerMethodField('get_job_name')
    job_company=serializers.SerializerMethodField('get_company_name')

    class Meta:
        model=JobenquiryC
        fields=['At','proposal','job_name','job_company']
    def get_job_name(self,info):
        data=info.job.job_title
        return data
    def get_company_name(self,info):
        data=info.job.by.Name
        return data