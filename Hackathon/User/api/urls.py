from .views import registration_view,activate,ObtainAuthTokenView,Resume
from django.urls import path
app_name='Account_api'
urlpatterns = [
    path('registration/',registration_view,name="registration"),
    path('activate/<uidb64>/<token>',activate,name="activate"),
    path('login/',ObtainAuthTokenView,name="login"),
    path('Resume/<int:id>',Resume)


]
