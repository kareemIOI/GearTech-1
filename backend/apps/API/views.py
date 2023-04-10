from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

class UserLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer_class = UserLoginSerializer
        print(serializer_class)
        queryset = User.objects.all()
        print(queryset)
        permission_classes = [permissions.AllowAny]
        # Handle GET requests here
        return Response({'message': 'This is a GET request'})

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'})
    
class UserLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'success': 'User has been logged out'})
