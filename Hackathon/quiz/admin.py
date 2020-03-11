from django.contrib import admin
from quiz.models import (
    Domain,
    Question,
    Answer,
    GeneralMarks,
    DomainQuestion,
    DomainMarks,
    DomainAnswer

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
@admin.register(GeneralMarks)
class PersonAdmin(ImportExportModelAdmin):
    pass
@admin.register(DomainQuestion)
class PersonAdmin(ImportExportModelAdmin):
    pass
@admin.register(DomainMarks)
class PersonAdmin(ImportExportModelAdmin):
    pass
@admin.register(DomainAnswer)
class PersonAdmin(ImportExportModelAdmin):
    pass
