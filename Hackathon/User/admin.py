from django.contrib import admin

# Register your models here.
from .models import user
from import_export.admin import ImportExportModelAdmin



@admin.register(user)
class PersonAdmin(ImportExportModelAdmin):
    pass