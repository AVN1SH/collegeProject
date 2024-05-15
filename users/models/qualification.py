from django.db import models
from users.models.registration import User_Model



class Qualifications_model(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    status=models.CharField(max_length=30,null=False)
    year=models.CharField(max_length=9,null=False)
    school=models.CharField(max_length=300,null=False)
    roll_code=models.CharField(max_length=10,null=False)
    total_marks=models.CharField(max_length=3,null=False)
    obtain_marks=models.CharField(max_length=3,null=False)