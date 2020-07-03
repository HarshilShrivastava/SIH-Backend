from django.contrib import admin

# Register your models here.
from .models import (
    Blogs,
    Courses
)
admin.site.register(Blogs)
admin.site.register(Courses)