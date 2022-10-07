from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserRegisterAPIView(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Index(View):

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ""
            user.save()
            return render(request, 'index.html', {})
        except User.DoesNotExist:
            return render(request, "dna.html", {})



class LoginAPIView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = LoginSerializer

    def get(self, request, email, format=None):
        users = User.objects.all()
        serializer = LoginSerializer(users)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutAPIView(APIView):
    def post(selfs, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class LoginJWTApiView(TokenObtainPairView):
#     serializer_class = LoginJWTSerializer



class LoginAPIView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutAPIView(APIView):
    def post(selfs, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class LoginApiView(TokenObtainPairView):
#     serializer_class = LoginSerializer

