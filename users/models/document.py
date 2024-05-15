from django.db import models
from users.models.registration import User_Model



class Document_model(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='documentation/photo/',null=False)
    signatue=models.ImageField(upload_to='documentation/signature/',null=False)
    adhar=models.FileField(upload_to='documentation/adhar/',null=False)
    tenth=models.FileField(upload_to='documentation/tenth/',null=False)
    twelth=models.FileField(upload_to='documentation/twelth/',null=False)