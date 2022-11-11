from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializer import RegisterSerializer


class UserRegistrationApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )


