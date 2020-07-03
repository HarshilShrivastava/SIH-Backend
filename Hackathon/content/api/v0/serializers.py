from rest_framework import serializers
from content.models import(
    Blogs,
    Courses
)

class BlogsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields=["Title","Description","photo","Refrences","Apply"]


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=["Title","Description","By","photo","Refrences","Apply"]