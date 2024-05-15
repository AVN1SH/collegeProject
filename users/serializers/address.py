from users.models.address import Address_Model
from rest_framework import serializers


class Address_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Address_Model
        fields="__all__"

    def create(self, validated_data):
        return Address_Model.objects.create(**validated_data)