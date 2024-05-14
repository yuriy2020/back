from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers import *


class CountryViewSet(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountryModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.order_by('id')
    serializer_class = UserModelSerializer


class CurrentUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('id')
    serializer_class = CurrentUserSerializer


class RegisterView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=user, email=email, password=password)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'status': status.HTTP_201_CREATED})


class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = request.data.get('username')
        # email = request.data.get('email')
        password = request.data.get('password')
        print('>>>', user, password)

        user = authenticate(request, username=user, password=password)
        print('>>>', user)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'status': status.HTTP_200_OK})
        else:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'})
