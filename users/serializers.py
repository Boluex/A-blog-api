from django.shortcuts import render
from .models import custom_user
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from rest_framework.views import Response


# Create your views here.

class register_serializer(ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = custom_user
        fields = ['username', 'email', 'password', 'password2', 'number']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        account = custom_user(username=self.validated_data['username'], email=self.validated_data['email'],
                              number=self.validated_data['number'])
        pass1 = self.validated_data['password']
        pass2 = self.validated_data['password2']

        if pass1 == pass2:
            account.set_password(pass1)
            account.save()
        else:
           return serializers.ValidationError()