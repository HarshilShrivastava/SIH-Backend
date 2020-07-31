from .models import (
    Recruit,
    Skill,
    JobenquiryC,
    GeneralMark,
    DomainMark,
    SubDomainMark,
    FulllistMarks,
    Certificate,
    Skills
    )
from rest_framework import serializers
import json
from Organization.models import SkillForJobs

class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model=SkillForJobs
        fields=['Name']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields=['Name']

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certificate
        fields=["Name","File"]

class FulllistMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model=FulllistMarks
        exclude=['Recruit']

class RecruitReadSerializer(serializers.ModelSerializer):
    R2=serializers.SerializerMethodField("get_residence")
    Skills=SkillsSerializer(many=True)
    class Meta:
        model=Recruit
        fields=["Name","Address","Resume","MarketRating","TechRating","Bio","Experience","Skills","Bio","R2","Familyincome","Time"]
    def get_residence(self,info):

        data= info.Residence.name
        return data

class RecruitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Recruit
        fields=["Name","Address","Resume",'Socialmedia',"Time","Familyincome","Residence","Bio","Experience"]
   
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
    get_candidate_skills=serializers.SerializerMethodField('get_can_skill')
    get_job_skills=serializers.SerializerMethodField('get_job_skill')

    class Meta:
        model=JobenquiryC
        fields=['proposal','At','Recruit_obj','Resume_obj','Recruit_add_obj','similarity','get_candidate_skills','get_job_skills']
    def get_can_skill(self,info):
        context={}
        data=info.Recruit.Skills.all()
        qs=skillSerializer(data,many=True)
        context=qs.data
        return context
    def get_job_skill(self,info):
        context={}
        print(info.Skills.all())
        data=info.job.SkillRequired.all()
        qs=skillSerializer(data,many=True)
        context=qs.data
        return context

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

class GeneralMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=GeneralMark
        fields=['Technology','Marketing','Total']


class DomainMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=DomainMark
        fields=['Domain','Total']

class subDomainMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubDomainMark
        fields=['SubDomain','Total']