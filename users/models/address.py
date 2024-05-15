from django.db import models
from users.models.registration import User_Model



class Address_Model(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    building_number=models.IntegerField()
    locality=models.CharField(max_length=50)
    sublocality=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    contract_number=models.CharField(max_length=10)
    alternate_number=models.CharField(max_length=10)