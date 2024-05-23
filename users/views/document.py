from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.document import Document_model
from users.serializers.document import Document_Serializers
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import requests

api_token = 'eac15c07239a1de0ce33ff58fc5d465e055b2902'
username = 'Arkas'
upload_path = '/home/Arkas/documentation/photo'

class Document_View(APIView):
    def get(self, request,pk=None, format=None):
        try:
            if pk is not None:
                user=Document_model.objects.get(pk=pk)
            else:
                user=Document_model.objects.all()
        except Document_model.DoesNotExist:
            return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        if pk is not None:
            serializer=Document_Serializers(user)
        else:
            serializer=Document_Serializers(user,many=True)
            print(serializer.data)
        return Response(serializer.data)
        return Response("Data not found",status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request,format=None):
        try:
            python_data=request.data
            rid=python_data.get('rid')
            user=Document_model.objects.filter(rid=rid)
            if user.exists():
                return Response("Personal Details save already",status=status.HTTP_400_BAD_REQUEST)
            
            python_data=request.data
            rid=python_data.get('rid')
            if rid=='' or rid==None:
                return Response("registration rid required",status=status.HTTP_204_NO_CONTENT)
            photo=python_data.get('photo')
            signatue=python_data.get('signatue')
            adhar=python_data.get('adhar')
            tenth=python_data.get('tenth')
            twelth=python_data.get('twelth')

            response = requests.post(
                f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path/{upload_path}',
                headers={'Authorization': f'Token {api_token}'},
                files={'file': photo}
            )
            if response.status_code == 200:
                print(response)
                print('File uploaded successfully')
            else:
                print(f'Failed to upload file: {response.status_code}, {response.text}')

            # python_data={
            #     'rid':rid,
            #     'photo':photo,
            #     'signatue':signatue,
            #     'adhar':adhar,
            #     'tenth':tenth,
            #     'twelth':twelth
            # }
            # serializer=Document_Serializers(data=python_data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response("Document Uploaded Successfully",status=status.HTTP_201_CREATED)
        except Document_model.DoesNotExist:
            return Response("Field not exits",status=status.HTTP_400_BAD_RESQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None,format=None):
        try:
            user=Document_model.objects.get(pk=pk)
            ri=Document_Serializers(user)
            python_data=request.data
            rid=python_data.get('rid')
            photo=python_data.get('photo')
            signatue=python_data.get('signatue')
            adhar=python_data.get('adhar')
            tenth=python_data.get('tenth')
            twelth=python_data.get('twelth')
            python_data={
                'rid':rid,
                'photo':photo,
                'signatue':signatue,
                'adhar':adhar,
                'tenth':tenth,
                'twelth':twelth
            }
            serializer=Document_Serializers(user,data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Document uploaded successfully",status=status.HTTP_201_CREATED)
        except Document_model.DoesNotExist:
            return Response("Field not found",status=status.HTTP_400_BAD_RESQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None,format=None):
        try:
            if pk==None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                user=Document_model.objects.get(pk=pk)
        except Document_model.DoesNotExist:
            return Response("Data not exits",status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("Documents deleted successfully",status=status.HTTP_204_NO_CONTENT)
    