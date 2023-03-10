from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view"""
    serializer_class=serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns alist of APIView features"""
        an_apiview=[
        'Uses HTTP meyhods as function (get, post, patch, put, delete)',
        'Is similar to traditional Django view',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create ahello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request,pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request,pk=None):
        """handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
