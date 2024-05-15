from django.db import models
from users.models.registration import User_Model


class Personal_Details(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=50,null=False)
    mother_name=models.CharField(max_length=50,null=False)
    sex=models.CharField(max_length=15,null=False)
    cast=models.CharField(max_length=15,null=False)
    dob=models.DateField()
    nationality=models.CharField(max_length=30,null=False)
    pwd=models.BooleanField(null=False)
