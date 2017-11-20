from rest_framework import serializers
#from rest_framework.validators import UniqueValidator
#from django.contrib.auth.models import User
from .models import Profile



class UserSerializer(serializers.ModelSerializer):
   # profilepic_url = serializers.ImageField(max_length=None,use_url =True,required =False)
    class Meta:
        model = Profile
        fields = ['username',
                  'email',
                  'password',
                  'firstname',
                  'lastname']






