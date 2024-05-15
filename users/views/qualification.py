from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.qualification import Qualifications_model
from users.serializers.qualification import Qualification_Serializers
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

class Qualification_View(APIView):
    def get(self, request,pk=None, format=None):
        try:
            if pk is not None:
                user=Qualifications_model.objects.get(pk=pk)
            else:
                user=Qualifications_model.objects.all()
        except Qualifications_model.DoesNotExist:
            return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        if pk is not None:
            serializer=Qualification_Serializers(user)
        else:
            serializer=Qualification_Serializers(user,many=True)
            print(serializer.data)
        return Response(serializer.data)
        return Response("Somethin went wrong , Try again ",status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,format=None):
        try:

            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            user=Qualifications_model.objects.filter(rid=rid)
            if user.exists():
                return Response("Personal Details save already",status=status.HTTP_400_BAD_REQUEST)



            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            status1=python_data.get('status')
            year=python_data.get('year')
            school=python_data.get('school')
            roll_code=python_data.get('roll_code')
            total_marks=python_data.get('total_marks')
            obtain_marks=python_data.get('obtain_marks')
            python_data={
                'rid':rid,
                'status':status1,
                'year':year,
                'school':school,
                'roll_code':roll_code,
                'total_marks':total_marks,
                'obtain_marks':obtain_marks
            }
            serializer=Qualification_Serializers(data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Qualification details save successfully !",status=status.HTTP_201_CREATED)
        except Qualifications_model.DoesNotExist:
            return Response("Field not exits",status=status.HTTP_400_BAD_RESQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None,format=None):
        try:
            user=Qualifications_model.objects.get(pk=pk)
            ri=Qualification_Serializers(user)
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            status1=python_data.get('status')
            year=python_data.get('year')
            school=python_data.get('school')
            roll_code=python_data.get('roll_code')
            total_marks=python_data.get('total_marks')
            obtain_marks=python_data.get('obtain_marks')
            python_data={
                'rid':rid,
                'status':status1,
                'year':year,
                'school':school,
                'roll_code':roll_code,
                'total_marks':total_marks,
                'obtain_marks':obtain_marks
            }
            serializer=Qualification_Serializers(user,data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Qualification update successfully",status=status.HTTP_201_CREATED)
        except Qualifications_model.DoesNotExist:
            return Response("Field not exits",status=status.HTTP_400_BAD_RESQUEST)
        return Response("Data not found !",status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None,format=None):
        try:
            if pk==None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                user=Qualifications_model.objects.get(pk=pk)
        except Qualifications_model.DoesNotExist:
            return Response("Data not exits",status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("Qualification details deleted successfully",status=status.HTTP_204_NO_CONTENT)
    