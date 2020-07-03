from .views import RecommendedBlogs,RecommendedCourses
from django.urls import path
urlpatterns = [

    path('Recommended-courses/',RecommendedCourses),
    path('Recommended-blogs/',RecommendedBlogs,name="food data"),

]