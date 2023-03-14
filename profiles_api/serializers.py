from rest_framework import serializers
from profiles_api import models


class HelloSerializers(serializers.Serializer):
    """serialzes is the name field for testing our API"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """serialzes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields= ('id','email','name','password')
        extra_kwards={
            'password':{
                'write_only': True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user= models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        )
        return user
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
