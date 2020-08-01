from django.contrib import admin
from .models import(
    Domain,
    SubDomain,
    Question,
    Answer
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


@admin.register(SubDomain)
class PersonAdmin(ImportExportModelAdmin):
    pass