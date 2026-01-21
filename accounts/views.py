from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import SignUpSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .tokens import create_jwt_pair_for_user
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class SignUpView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = SignUpSerializer

    @swagger_auto_schema(
            operation_summary = "Creates a user account",
            
    )
    def post(self,request:Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message" : "User Created Successfully",
                "data" : serializer.data
            }

            return Response(data = response,status = status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    permission_classes = []


    @swagger_auto_schema(
            operation_summary = "login to a account by creating  a JWT pair",
            
    )
    def post(self,request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email,password=password)

        if user is not None:

            tokens = create_jwt_pair_for_user(user)
            response = {
                "message" : "Login successfull",
                "tokens" : tokens
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        else:
            return Response(data={"message":"Invalid email/password"})



    @swagger_auto_schema(
            operation_summary = "Get request info",
            operation_description="this shows the request information"
            
    )
    def get(self,request:Request):
        content = {
            "user" : str(request.user),
            "auth" : str(request.auth)

        }
        return Response(data=content,status=status.HTTP_200_OK)
    