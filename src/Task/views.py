#from rest_framework import status
#from accounts.serializers import UserSerializer
from django.contrib.auth.models import User


from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import Profile
from .serializers import UserSerializer
#from rest_framework.permissions import IsAuthenticated


##### Create API VIEWS ####
class UserViewSet(viewsets.ModelViewSet):
    #DEFAULT_PERMISSION_CLASSES =(IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UserSerializer




