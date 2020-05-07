from django.contrib import admin
from .models import Company,Jobs
from import_export.admin import ImportExportModelAdmin
@admin.register(Jobs)
class PersonAdmin(ImportExportModelAdmin):
    pass


@admin.register(Company)
class PersonAdmin(ImportExportModelAdmin):
    pass
