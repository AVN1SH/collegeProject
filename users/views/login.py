from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.registration import User_Model
from users.serializers.login import Login_Serializers
from users.serializers.registration import User_Serializers
import random
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view

class Login_View(APIView):
        def post(self, request, format=None):
            try:
                json_data=request.body
                stream=io.BytesIO(json_data)
                python_data=JSONParser().parse(stream)
                email=python_data.get('email')
                if email=='' or email==None:
                     return Response("Email is required",status=status.HTTP_204_NO_CONTENT)
                password=python_data.get('password')
                if password=='' or password==None :
                     return Response("Password is required ",status=status.HTTP_204_NO_CONTENT)
                


                
                user=User_Model.objects.all()
                serializer=User_Serializers(user,many=True)
                em=serializer.data
                k=0
                print(em)
                for i in em:
                     print(i['email'])
                     if email==i['email'] and check_password(password,i['password']):
                          print("Hello")
                          record={
                                   'id':i['id'],
                                   'registration_id':i['registration_id'],
                                   'first_name':i['first_name'],
                                   'middle_name':i['middle_name'],
                                   'last_name':i['last_name'],
                                   'role':i['role'],
                                   'phone':i['phone'],
                                   'email':i['email'],
                                   }
                          k=1
                          break
                if k==0:
                     return Response("user id or password not matching ",status=status.HTTP_204_NO_CONTENT)
                print(record)
                if i is not None:
                     return Response(record,status=status.HTTP_202_ACCEPTED)
                
            except User_Model.DoesNotExist:
                return Response("User id and passwrord",status=status.HTTP_404_NOT_FOUND)
            return Response("user id or password not matchiing.",status=status.HTTP_404_NOT_FOUND)