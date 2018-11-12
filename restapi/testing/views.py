from django.shortcuts import render
from rest_framework import viewsets
from testing.models import User
from testing.serializers import UserSerializers
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class =UserSerializers