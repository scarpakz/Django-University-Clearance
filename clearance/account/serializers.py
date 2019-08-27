from rest_framework import serializers
from .models import Clearance, ClearanceStatus
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClearanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clearance
        fields = ['request']

class ClearanceAddRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clearance
        fields = '__all__'