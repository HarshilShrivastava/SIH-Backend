from django.contrib import admin
from quiz.models import (
    Domain,
    Question,
    Answer,
    DomainQuestion,
    DomainAnswer,
    SubDomain

)
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Domain)
class PersonAdmin(ImportExportModelAdmin):
    pass
@admin.register(Question)
class PersonAdmin(ImportExportModelAdmin):
    pass
@admin.register(Answer)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(DomainQuestion)
class PersonAdmin(ImportExportModelAdmin):
    list_filter = ('SubDomain', 'Level3')
    pass

@admin.register(DomainAnswer)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(SubDomain)
class PersonAdmin(ImportExportModelAdmin):
    pass
