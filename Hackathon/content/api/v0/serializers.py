from rest_framework import serializers
from content.models import(
    Blogs,
    Courses,
    Scheme
)

class BlogsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields="__all__"


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields="__all__"


class SchemeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Scheme
        fields="__all__"