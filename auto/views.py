from django.shortcuts import render
from rest_framework import generics, status
from .models import *
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import requests
import os

class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


TELEGRAM_BOT_TOKEN = "7809374705:AAEe8f2IDVAwY_LpUuhlpip4MTNX5zyMCBQ"
TELEGRAM_CHAT_ID = "-1002502786746"


@method_decorator(csrf_exempt, name='dispatch')
class PurchaseRequisitionView(generics.ListCreateAPIView):
    serializer_class = PurchaseRequisitionSerializer
    queryset = PurchaseRequisition.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            purchase = serializer.save()
            try:
                message = (
                    f"💬 *Новая заявка от клиента!*\n\n"
                    f"👤 *Имя* {purchase.name}\n"
                    f"📞 *Телефон* {purchase.phone_number}\n"
                )

                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message,
                    "parse_mode": "Markdown"
                }

                response = requests.post(url, json=payload)

                if response.status_code == 200:
                    print("✅ Сообщение успешно отправлено!")
                else:
                    print(f"⚠️ Ошибка при отправке сообщения. Ответ: {response.text}")

            except Exception as e:
                print(f"❌ Ошибка отправки сообщения в Telegram: {e}")
                return Response({"Ошибка": "Не удалось отправить сообщение в Telegram"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


