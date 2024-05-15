from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.address import Address_Model
from users.serializers.address import Address_Serializers
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password,check_password

class Address_View(APIView):
    def get(self, request,pk=None, format=None):
        try:
            if pk is not None:
                user=Address_Model.objects.get(pk=pk)
            else:
                user=Address_Model.objects.all()
        except Address_Model.DoesNotExist:
            return Response("Data not found !",status=status.HTTP_404_NOT_FOUND)
        if pk is not None:
            serializer=Address_Serializers(user)
        else:
            serializer=Address_Serializers(user,many=True)
        return Response(serializer.data)
        return Response(Address_Model.erros,status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,format=None):
        try:

            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            user=Address_Model.objects.filter(rid=rid)
            if user.exists():
                return Response("Personal Details save already",status=status.HTTP_400_BAD_REQUEST)

            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            building_number=python_data.get('building_number')
            locality=python_data.get('locality')
            sublocality=python_data.get('sublocality')
            state=python_data.get('state')
            district=python_data.get('district')
            pincode=python_data.get('pincode')
            contract_number=python_data.get('contract_number')
            alternate_number=python_data.get('alternate_number')
            python_data={
                'rid':rid,
                'building_number':building_number,
                'locality':locality,
                'sublocality':sublocality,
                'state':state,
                'district':district,
                'pincode':pincode,
                'contract_number':contract_number,
                'alternate_number':alternate_number
            }
            print(python_data)
            serializer=Address_Serializers(data=python_data)
            print(serializer)
            if serializer.is_valid():
                print("hello")
                serializer.save()
                return Response("Address save successfully",status=status.HTTP_201_CREATED)
        except Address_Model.DoesNotExist:
            return Response("Field not exits",status=status.HTTP_400_BAD_RESQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None,format=None):
        try:
            user=Address_Model.objects.get(pk=pk)
            ri=Address_Serializers(user)
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            rid=python_data.get('rid')
            building_number=python_data.get('building_number')
            locality=python_data.get('locality')
            sublocality=python_data.get('sublocality')
            state=python_data.get('state')
            district=python_data.get('district')
            pincode=python_data.get('pincode')
            contract_number=python_data.get('contract_number')
            alternate_number=python_data.get('alternate_number')
            python_data={
                'rid':rid,
                'building_number':building_number,
                'locality':locality,
                'sublocality':sublocality,
                'state':state,
                'district':district,
                'pincode':pincode,
                'contract_number':contract_number,
                'alternate_number':alternate_number
            }
            serializer=Address_Serializers(user,data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Address updated successfully",status=status.HTTP_201_CREATED)
        except Address_Model.DoesNotExist:
            return Response("Data not found !",status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None,format=None):
        try:
            if pk==None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                user=Address_Model.objects.get(pk=pk)
        except Address_Model.DoesNotExist:
            return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("Address Deleted successfully",status=status.HTTP_204_NO_CONTENT)