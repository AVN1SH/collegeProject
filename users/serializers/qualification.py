from users.models.qualification import Qualifications_model
from rest_framework import serializers


class Qualification_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Qualifications_model
        fields="__all__"

    def create(self, validated_data):
        return Qualifications_model.objects.create(**validated_data)