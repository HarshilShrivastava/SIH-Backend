from django.contrib import admin
from .models import Recruit,Skill,JobenquiryC,GeneralMark,DomainMark,SubDomainMark,FulllistMarks
admin.site.register(Recruit)
admin.site.register(Skill)
admin.site.register(JobenquiryC)
admin.site.register(GeneralMark)
admin.site.register(FulllistMarks)
admin.site.register(DomainMark)
admin.site.register(SubDomainMark)

# Register your models here.
