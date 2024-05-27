from django.db import models
from users.models.registration import User_Model



class Document_model(models.Model):
    rid=models.ForeignKey(User_Model,on_delete=models.CASCADE)
    photo=models.charField()
    signatue=models.charField()
    adhar=models.charField()
    tenth=models.charField()
    twelth=models.charField()