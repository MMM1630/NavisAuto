from django.contrib import admin
from django.contrib.admin import TabularInline
from auto.models import *

# class CarPhotoInline в админке нужно для связки моделей в админ понели и для удобства
# model, для того чтобы указать модель из /NavisAuto/auto/models
# extra с указанным значением 1 для того чтобы default было одно поля, но есть возможность добавить еще

class CarPhotoInline(TabularInline):
    model = CarPhoto
    extra = 1

# @admin.register(Car) для регистрации модели Car в админке
# class Car это админка для модели Car из /NavisAuto/auto/models
# list_filter нужен для удобства в админке для того чтобы можно было искать авто по его значением в моем случаи его значения ("name", "company", "year", "available")
# важно примечание для всех полей обязательно каждое значение должен присутствовать в models в которого вы зарегистрировали
# list_display это поля для вывода значений которых вы указали в нем
# list_editable дает возможность менять какое-то значение прямо в дисплее в моем случае это available чтобы я мог поменять его значение из True на False наоборот тоесть указать есть ли данный авто в наличии
# inlines добавит его в нашу админку и выдаст ему отдельную страницу
# fieldsets для деления одной модели на две части тоесть будет две страницы в моем случае Машины и Характеристики машины

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ("name", "company", "year", "available")
    list_display = ("name", "company", "type", "year", "available")
    list_editable = ("available",)
    inlines = [CarPhotoInline]
    fieldsets = [
        (
            "Машины",
            {
                "fields": ["available" ,"name", "company", "img", "year", "type", "state",  "contribution", "price", "time", "title_price"],
            },
        ),
        (
            "Характеристики машины",
            {
                "classes": ["collapse"],
                "fields": ["registration_type", "registration_date", "motor", "KPP", "fuel", "drive", "mileage", "color", "VIN_code"],
            },
        ),
    ]


# admin.register(PurchaseRequisition) для регистрации в админке
# class это админка для модели PurchaseRequisition
# list_display для вывода значений в лицевую сторону в админке
# данная админка нужна для контроля сообщении от клиентов

@admin.register(PurchaseRequisition)
class PurchaseRequisitionAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")


# admin.register(Contact) для регистрации в админке
# class это админка для модели Contact
# list_display для вывода значений в лицевую сторону в админке
# данная админка нужна, чтобы менять значение в случае переезда

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("city", "locations", "phone_number")