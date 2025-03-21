
from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
# for sending email

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework .decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializers



class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class =serializers.UserSerializer



class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"https://ecommerce-backend-4yjb.onrender.com/account/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)



def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


class UserLoginApiView(APIView):
    def post(self, request):
        user_login_serializer = serializers.UserLoginSerializer(data=request.data)
        
        if user_login_serializer.is_valid():
            username = user_login_serializer.validated_data['username']
            password = user_login_serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Invalid Credential"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(user_login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogoutApiView(APIView):
    def get(self, request):
        logout(request)
        return redirect('login')
    


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers





    