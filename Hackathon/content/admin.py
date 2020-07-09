from django.contrib import admin

# Register your models here.
from .models import (
    Blogs,
    Courses,
    Scheme,
)
admin.site.register(Blogs)
admin.site.register(Courses)
admin.site.register(Scheme)