from .views import (
    RecommendedBlogs,
    RecommendedCourses,
    RecommendedScheme,
    AllBlogsViews,
    AllSchemeViews,
    CoursesViews,
    )
from django.urls import path
urlpatterns = [

    path('Recommended-courses/',RecommendedCourses),
    path('Recommended-blogs/',RecommendedBlogs),
     path('Recommended-Scheme/',RecommendedScheme),
     path('scheme-search',AllSchemeViews.as_view()),
      path('blogs-search',AllBlogsViews.as_view()),
     path('course-search',CoursesViews.as_view()),
     

]