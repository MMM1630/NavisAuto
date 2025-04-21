from rest_framework import serializers
from urllib3 import request
from .models import *


class CarSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = "__all__"

    def get_img(self, obj):
        request = self.context.get("request")
        img_queryset = CarPhoto.objects.filter(car=obj)
        return [{"photo_car": request.build_absolute_uri(img.img.url)} for img in img_queryset if img.img]

    def validate(self, data):
        reg_type = data.get('registration_type')
        reg_date = data.get('registration_date')

        if reg_type in [CarRegistrationType.PRIMARY, CarRegistrationType.SECONDARY] and not reg_date:
            raise serializers.ValidationError({
                'registration_date': 'Необходимо указать дату регистрации.'
            })
        return data

class PurchaseRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequisition
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"