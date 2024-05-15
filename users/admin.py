from django.contrib import admin
from users.models.registration import User_Model
from users.models.personalDetails import Personal_Details
from users.models.address import Address_Model
from users.models.qualification import Qualifications_model
from users.models.document import Document_model


@admin.register(User_Model)
class User_Admin(admin.ModelAdmin):
    list_display=['id',
                  'registration_id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'role',
                  'phone',
                  'email',
                  'password']
    ordering=['id']

@admin.register(Personal_Details)
class User_Admin(admin.ModelAdmin):
    list_display=['id',
                  'rid',
                  'father_name',
                  'mother_name',
                  'sex',
                  'cast',
                  'dob',
                  'nationality',
                  'pwd']
    ordering=['id']

@admin.register(Address_Model)
class Address_Admin(admin.ModelAdmin):
    list_display=['id',
                  'rid',
                  'building_number',
                  'locality',
                  'sublocality',
                  'state',
                  'district',
                  'pincode',
                  'contract_number',
                  'alternate_number']
    ordering=['id']

@admin.register(Qualifications_model)
class Qualifications_Admin(admin.ModelAdmin):
    list_display=['rid',
                  'status',
                  'year',
                  'school',
                  'roll_code',
                  'total_marks',
                  'obtain_marks'
                  ]

@admin.register(Document_model)
class Document_Admin(admin.ModelAdmin):
    list_display=['rid',
                  'photo',
                  'signatue',
                  'adhar',
                  'tenth',
                  'twelth'
                  ]