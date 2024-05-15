from django.db import models


class User_Model(models.Model):
    id=models.AutoField(primary_key=True)
    registration_id = models.CharField(max_length=15,null=False)
    first_name = models.CharField(max_length=30,null=False)
    middle_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    role = models.CharField(max_length=30,null=False)
    phone = models.CharField(max_length=10,null=False)
    email = models.EmailField(unique=False)
    password = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.registration_id