from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns alist of APIView features"""
        an_apiview=[
        'Uses HTTP meyhods as function (get, post, patch, put, delete)',
        'Is similar to traditional Django view',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
