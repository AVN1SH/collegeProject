from users.models.document import Document_model
from rest_framework import serializers


class Document_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Document_model
        fields="__all__"

    def create(self, validated_data):
        return Document_model.objects.create(**validated_data)