from .views import RecommendedBlogs,RecommendedCourses,RecommendedScheme
from django.urls import path
urlpatterns = [

    path('Recommended-courses/',RecommendedCourses),
    path('Recommended-blogs/',RecommendedBlogs),
     path('Recommended-Scheme/',RecommendedScheme),

]