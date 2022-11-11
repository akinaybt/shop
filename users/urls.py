from django.urls import path, include
from .views import UserRegistrationApiView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('auth/', ObtainAuthToken.as_view()),
    path('register/', UserRegistrationApiView.as_view()),
]
