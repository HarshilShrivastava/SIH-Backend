from django.contrib import admin
from .models import Recruit,Skill,JobenquiryC,GeneralMark,DomainMark,SubDomainMark,FulllistMarks,SocialMedia,SocialMediaTags,Residence,SocioeconomicTags,Certificate,Skills,JobStatus
admin.site.register(Recruit)
admin.site.register(Skill)
admin.site.register(JobenquiryC)
admin.site.register(GeneralMark)
admin.site.register(FulllistMarks)
admin.site.register(DomainMark)
admin.site.register(SocialMedia)
admin.site.register(SubDomainMark)
admin.site.register(SocialMediaTags)
admin.site.register(Residence)
admin.site.register(SocioeconomicTags)
admin.site.register(JobStatus)

admin.site.register(Certificate)

admin.site.register(Skills)
# Register your models here.
