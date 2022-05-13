from dataclasses import fields
from pyexpat import model
from ..models import Message
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','date_joined','last_login')

class MessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True) # Need to declare read_only true in order for it to work.
    # because if we don't declare then it thinks that we need to provide created_by field in json format

    class Meta:
        model = Message
        fields = '__all__'
        extra_kwargs = {"created_by": {"required": False}}
