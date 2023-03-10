from rest_framework import serializers



class HelloSerializers(serializers.Serializer):
    """serialzes is the name field for testing our API"""
    name = serializers.CharField(max_length=10)
    
