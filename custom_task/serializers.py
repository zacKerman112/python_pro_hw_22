from rest_framework import serializers
from .models import UserConfig, UserLog

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = '__all__'
        

class UserConfigSerializer(serializers.ModelSerializer):
    logs = UserLogSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserConfig
        fields = '__all__'