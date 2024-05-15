from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.personalDetails import Personal_Details
from users.serializers.personalDetails import Persona_Details_Serializers
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from users.models.registration import User_Model
from users.serializers.registration import User_Serializers

class Personal_Details_View(APIView):
    def get(self, request,pk=None, format=None):
        try:
            if pk is not None:
                user=Personal_Details.objects.get(pk=pk)
            else:
                user=Personal_Details.objects.all()
        except Personal_Details.DoesNotExist:
            return Response("Data Not Found !",status=status.HTTP_404_NOT_FOUND)
        if pk is not None:
            serializer=Persona_Details_Serializers(user)
        else:
            serializer=Persona_Details_Serializers(user,many=True)
        return Response(serializer.data)
        return Response("Something went wrong ",status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,pk=None,format=None):
        try:
            
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            user=Personal_Details.objects.filter(rid=rid)
            if user.exists():
                return Response("Personal Details save already",status=status.HTTP_400_BAD_REQUEST)
            
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            father_name=python_data.get('father_name')
            mother_name=python_data.get('mother_name')
            new_email=python_data.get('email')
            new_phone=python_data.get('phone')
            sex=python_data.get('sex')
            cast=python_data.get('cast')
            dob=python_data.get('dob')
            nationality=python_data.get('nationality')
            pwd=python_data.get('pwd')


            user=User_Model.objects.get(pk=rid)
            serializer=User_Serializers(user)
            updaate_email=serializer.data
            registration_id=updaate_email['registration_id']
            first_name=updaate_email['first_name']
            middle_name=updaate_email['middle_name']
            last_name=updaate_email['last_name']
            role=updaate_email['role']
            phone=updaate_email['phone']
            email=updaate_email['email']
            password=updaate_email['password']
            if email!=new_email:
                print(email)
                print(new_email)
                email=new_email
                updaate_email={
                'registration_id':registration_id,
                'first_name':first_name,
                'middle_name':middle_name,
                'last_name':last_name,
                'role':role,
                'phone':phone,
                'email':email,
                'password':password}
                serializer=User_Serializers(user,data=updaate_email)
                if serializer.is_valid():
                    serializer.save()
            if phone!=new_phone:
                print(email)
                print(new_email)
                email=new_email
                updaate_email={
                'registration_id':registration_id,
                'first_name':first_name,
                'middle_name':middle_name,
                'last_name':last_name,
                'role':role,
                'phone':new_phone,
                'email':new_email,
                'password':password}
                serializer=User_Serializers(user,data=updaate_email)
                if serializer.is_valid():
                    serializer.save()



            python_data={
                'rid':rid,
                'father_name':father_name,
                'mother_name':mother_name,
                'sex':sex,
                'cast':cast,
                'dob':dob,
                'nationality':nationality,
                'pwd':pwd,
            }
            serializer=Persona_Details_Serializers(data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Personal Details save Successfully",status=status.HTTP_201_CREATED)
        except Personal_Details.DoesNotExist:
            return Response("Personal Details Note save",status=status.HTTP_400_BAD_RESQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None,format=None):
        try:
            user=Personal_Details.objects.get(pk=pk)
            ri=Persona_Details_Serializers(user)
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            father_name=python_data.get('father_name')
            mother_name=python_data.get('mother_name')
            sex=python_data.get('sex')
            cast=python_data.get('cast')
            dob=python_data.get('dob')
            nationality=python_data.get('nationality')
            pwd=python_data.get('pwd')
            python_data={
                'rid':rid,
                'father_name':father_name,
                'mother_name':mother_name,
                'sex':sex,
                'cast':cast,
                'dob':dob,
                'nationality':nationality,
                'pwd':pwd,
            }
            serializer=Persona_Details_Serializers(user,data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Personal Details updated successfully",status=status.HTTP_201_CREATED)
        except Personal_Details.DoesNotExist:
            return Response(serializer.errors,status=status.HTTP_400_BAD_RESQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None,format=None):
        try:
            if pk==None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                user=Personal_Details.objects.get(pk=pk)
        except Personal_Details.DoesNotExist:
            return Response("Data not found on this id",status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("Personal Data deleted successfully !",status=status.HTTP_204_NO_CONTENT)
    