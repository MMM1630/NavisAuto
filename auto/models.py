from django.db import models
from django.db.models import *
from auto.choices import *


# models Car для добавления авто с полными характеристиками тут есть:
# available для обозначения авто в наличии или нет
# name название авто, мол, Camry и тому подобное для удобства
# title_price для обозначения суммы как Ежемесячный платеж за авто
# company для обозначения компании производителя, мол, Тайота
# year это год в котором выпускалась авто
# state это состояние авто для обозначения новое или нет
# contribution первоначальный взнос за авто если она в кредит
# time срок для кредита, мол, 60 месяцев и тому подобное
# price это цена авто

# дальше идут характеристики и подробная информация

# registration_type регистрация первичная или вторична для выбора используется Choices который в отдельном файле
# registration_date дата регистрации обязательно к заполнению
# motor тип мотора который стоит на продаже
# KPP это тип коробки передач автомат или механическая коробка передач
# fuel это тип топлива для авто
# drive это ведущая ось или же привод
# mileage показание одометра или по другому пробег авто
# color это цвет автомобиля
# VIN_code это уникальный идентификатор транспортного средства, состоящий из 17 символов, который используется для его регистрации и отслеживания


class Car(models.Model):
    available = models.BooleanField("В наличие")
    name = models.CharField("Модель машины", max_length=20)
    title_price = models.CharField("Ежемесячный платеж", max_length=20)
    company = models.CharField("Компания производитель", max_length=20)
    type = models.CharField("Тип машина", max_length=20)
    year = models.IntegerField("Год выпуска")
    state = models.CharField("Состояние", max_length=20)
    contribution = models.CharField("Первоначальный взнос", max_length=20)
    time = models.CharField("Срок", max_length=20)
    price = models.CharField("Цена", max_length=20)
    # подробнее
    registration_type = models.CharField("Регистрация",max_length=10,choices=CarRegistrationType.choices)
    registration_date = models.DateField("Дата регистрации",null=True, blank=True)
    motor = models.CharField("Двигатель", max_length=50)
    KPP = models.CharField("КПП", max_length=20)
    fuel = models.CharField("Тип топлива", max_length=20)
    drive = models.CharField("Ведущая ось(Привод)", max_length=20)
    mileage = models.CharField("Показания одометра (Пробег)", max_length=20)
    color = models.CharField("Цвет", max_length=20)
    VIN_code = models.CharField("VIN код", max_length=20)


# Class Meta: это вложенный класс, который используется для настройки поведения модели
#     verbose_name: человеко читаемое название модели в единственном числе, используемое в административной панели и документации.
#     Verbose_name_plural: человеко читаемое название модели в множественном числе, используемое в административной панели и документации.

    class Meta:
        verbose_name = "Автомобили"
        verbose_name_plural = "Автомобили"

#   Def: ключевое слово в Python для объявления функции или метода.
#   __str__:специальный метод, который возвращает строковое представление объекта, обычно используется для отображения в админке и логах.
#   Self: ссылка на текущий экземпляр класса, используется внутри методов.
#   Return : оператор для возврата значения из функции или метода
#   F строка: способ форматирования строк в Python с подстановкой переменных

    def __str__(self):
        return f"{self.registration_type} — {self.registration_date or 'Дата не указана'}"

# class CarPhoto нужен для того чтобы в админке была возможность связывать их между собой что дает примущества в ввиде поля куда можно добавлять 1 или больше фотографий
# car для связки моделей с помощью ForeignKey
# img поля для фото

class CarPhoto(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    img = models.ImageField("Фото авто")

# Class Meta: это вложенный класс, который используется для настройки поведения модели
#     verbose_name: человеко читаемое название модели в единственном числе, используемое в административной панели и документации.
#     Verbose_name_plural: человеко читаемое название модели в множественном числе, используемое в административной панели и документации.

    class Meta:
        verbose_name = "Фото машины"
        verbose_name_plural = "Фото машины"


# class Purchase Requisition для отправки сообщений в Telegram
# name это ФИО клиента
# phone number это номер телефона клиента

class PurchaseRequisition(models.Model):
    name = CharField("Имя Фамилия", max_length=40)
    phone_number = IntegerField("Ваш номер телефона")

# Class Meta: это вложенный класс, который используется для настройки поведения модели
#     verbose_name: человеко читаемое название модели в единственном числе, используемое в административной панели и документации.
#     Verbose_name_plural: человеко читаемое название модели в множественном числе, используемое в административной панели и документации.

    class Meta:
        verbose_name = "Заявка на покупку авто"
        verbose_name_plural = "Заявка на покупку авто"

# class Contact это модель контактов от сайта
# city поля для обозначения города
# locations поля для обозначения адреса
# phone number поля обозначения телефонного номера для владельца авто чтобы с ним могли связаться клиенты

class Contact(models.Model):
    city = models.CharField("Город", max_length=20)
    locations = models.CharField("Локация", max_length=40)
    phone_number = models.IntegerField("Номер телефона")

# Class Meta: это вложенный класс, который используется для настройки поведения модели
#     verbose_name: человеко читаемое название модели в единственном числе, используемое в административной панели и документации.
#     Verbose_name_plural: человеко читаемое название модели в множественном числе, используемое в административной панели и документации.

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"