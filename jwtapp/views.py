# accounts/views.py

from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class Register(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

class UserLogin(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(request.data)
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            print(refresh)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token,'refresh':str(refresh)}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)



class LogOut(APIView): 
    permission_classes=[IsAuthenticated]
    def post(self,request):
            refresh_token = RefreshToken(request.data.get("refresh_token"))
            refresh_token.blacklist()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)


    