from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.address import Address_Model
from users.models.document import Document_model
from users.models.personalDetails import Personal_Details
from users.models.qualification import Qualifications_model
from users.models.registration import User_Model
from users.serializers.address import Address_Serializers
from users.serializers.document import Document_Serializers
from users.serializers.personalDetails import Persona_Details_Serializers
from users.serializers.qualification import Qualification_Serializers
from users.serializers.registration import User_Serializers
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

class All_Data_View(APIView):
    def get(self, request,pk=None, format=None):
        try:
            if pk is not None:
                user=User_Model.objects.get(pk=pk)
                serializer=User_Serializers(user)
                python_data=serializer.data
                registration_id=python_data['registration_id']
                first_name=python_data['first_name']
                middle_name=python_data['middle_name']
                last_name=python_data['last_name']
                role=python_data['role']
                phone=python_data['phone']
                email=python_data['email']


                user=Personal_Details.objects.get(rid=pk)
                serializer=Persona_Details_Serializers(user)
                python_data=serializer.data
                father_name=python_data['father_name']
                mother_name=python_data['mother_name']
                sex=python_data['sex']
                cast=python_data['cast']
                dob=python_data['dob']
                nationality=python_data['nationality']

                user=Address_Model.objects.get(rid=pk)
                serializer=Address_Serializers(user)
                python_data=serializer.data
                building_number=python_data['building_number']
                locality=python_data['locality']
                sublocality=python_data['sublocality']
                state=python_data['state']
                district=python_data['district']
                pincode=python_data['pincode']
                contract_number=python_data['contract_number']
                alternate_number=python_data['alternate_number']

                print("Hello")
                user=Qualifications_model.objects.get(rid=pk)
                serializer=Qualification_Serializers(user)
                python_data=serializer.data
                status1=python_data['status']
                year=python_data['year']
                school=python_data['school']
                roll_code=python_data['roll_code']
                total_marks=python_data['total_marks']
                obtain_marks=python_data['obtain_marks']

                user=Document_model.objects.get(rid=pk)
                serializer=Document_Serializers(user)
                python_data=serializer.data
                photo=python_data['photo']
                signatue=python_data['signatue']
                adhar=python_data['adhar']
                tenth=python_data['tenth']
                twelth=python_data['twelth']


                data={
                    'registration_id':registration_id,
                    'first_name':first_name,
                    'middle_name':middle_name,
                    'last_name':last_name,
                    'role':role,
                    'phone':phone,
                    'email':email,
                    'father_name':father_name,
                    'mother_name':mother_name,
                    'sex':sex,
                    'cast':cast,
                    'dob':dob,
                    'nationality':nationality,
                    'building_number':building_number,
                    'locality':locality,
                    'sublocality':sublocality,
                    'state':state,
                    'district':district,
                    'pincode':pincode,
                    'contract_number':contract_number,
                    'alternate_number':alternate_number,
                    'status':status1,
                    'year':year,
                    'school':school,
                    'roll_code':roll_code,
                    'total_marks':total_marks,
                    'obtain_marks':obtain_marks,
                    'photo':photo,
                    'signature':signatue,
                    'adhar':adhar,
                    'tenth':tenth,
                    'twelth':tenth,

                }
                return Response(data)
        except :
            return Response("Data not founded",status=status.HTTP_400_BAD_REQUEST)
