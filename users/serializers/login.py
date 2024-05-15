from users.models.registration import User_Model
from rest_framework import serializers

class Login_Serializers(serializers.ModelSerializer):
    class Meta:
        model=User_Model
        fields = ['id', 'email', 'password']
        
    # def create(self, validated_data):
    #     return User_Model.objects.create(**validated_data)