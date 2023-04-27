from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
            'online',
            'offline',
            'mutual',
            'external'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'PUT is working now'})

    def patch(self, request, pk=None):
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'Delete'})


class HelloViewStes(viewsets.ViewSet):
    """Test Api view sets"""
    serializer_class = serializers.HelloSerializer

    def lists(self, request):
        """Return hello list"""
        a_viewSet = [
            'Users Action 1',
            'Users Action 2',
            'Users Action 3',
            'Users Action 4',
            'Users Action 5',
        ]
        return Response({
            'message': 'Hello',
            'a_viewser': a_viewSet,
        })

    def create(self, request):
        """Create a new hello message"""
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            message = f'Hello {name}'
            return Response({
                message: message
            })
        else:
            return Response(
                serializers.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """Handel Getting an object by its ID"""
        return Response({'http_method': 'Get'})

    def update(self, request, pk=None):
        return Response({'http_method': 'Update'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'Patch'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles user  feeds"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.profileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnFeed, IsAuthenticated,)

    def perform_create(self, serializer):
        """set the profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
