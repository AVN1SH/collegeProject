from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.registration import User_Model
from users.serializers.registration import User_Serializers
import random
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

def account():
    num=random.randrange(0000000,9999999)
    num="AV/2024/"+str(num)
    if len(num)==15:
        return num
class User_View(APIView):
    def get(self, request,pk=None, format=None):
        try:
            if pk is not None:
                user=User_Model.objects.get(pk=pk)
            else:
                user=User_Model.objects.all()
        except User_Model.DoesNotExist:
            return Response("Data not found !",status=status.HTTP_404_NOT_FOUND)
        if pk is not None:
            serializer=User_Serializers(user)
        else:
            serializer=User_Serializers(user,many=True)
        return Response(serializer.data)
        return Response("Data format not matching",status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,format=None):
        try:
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            first_name=python_data.get('first_name')
            middle_name=python_data.get('middle_name')
            print("vikas")
            print(middle_name)
            print("Hello")
            if middle_name==None or middle_name=="":
                middle_name=None
                print(middle_name)
            last_name=python_data.get('last_name')
            if last_name==None or last_name=="":
                last_name=None
                print(last_name)
            role=python_data.get('role')
            phone=python_data.get('phone')
            email=python_data.get('email')
            password=python_data.get('password')
            if password==None or password=="":
                return Response("Password is required",status=status.HTTP_204_NO_CONTENT)
            password=make_password(password)
            user=User_Model.objects.filter(email=email)
            if user.exists():
                return Response("Email already exits",status=status.HTTP_400_BAD_REQUEST)
            python_data={
            'registration_id':account(),
            'first_name':first_name,
            'middle_name':middle_name,
            'last_name':last_name,
            'role':role,
            'phone':phone,
            'email':email,
            'password':password
            }
            print(python_data)
            serializer=User_Serializers(data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Register Successfully",status=status.HTTP_201_CREATED)
        except User_Model.DoesNotExist:
            return Response("Field not exits",status=status.HTTP_400_BAD_RESQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None,format=None):
        try:
            user=User_Model.objects.get(pk=pk)
            ri=User_Serializers(user)
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            first_name=python_data.get('first_name')
            middle_name=python_data.get('middle_name')
            last_name=python_data.get('last_name')
            role=python_data.get('role')
            phone=python_data.get('phone')
            email=python_data.get('email')
            password=make_password(python_data.get('password'))
            python_data={
                'registration_id':ri.data.get('registration_id'),
                'first_name':first_name,
                'middle_name':middle_name,
                'last_name':last_name,
                'role':role,
                'phone':phone,
                'email':email,
                'password':password
            }
            serializer=User_Serializers(user,data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Registration updated successfully",status=status.HTTP_201_CREATED)
        except User_Model.DoesNotExist:
            return Response("Field not exits",status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk=None,format=None):
        try:
            if pk==None:
                return Response("Please enter user id",status=status.HTTP_404_NOT_FOUND)
            else:
                user=User_Model.objects.get(pk=pk)
        except User_Model.DoesNotExist:
            return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("Date deleted Successfully",status=status.HTTP_204_NO_CONTENT)