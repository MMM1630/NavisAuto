from django.db import models

class CarRegistrationType(models.TextChoices):
    PRIMARY = 'primary', 'Первичная регистрация'
    SECONDARY = 'secondary', 'Вторичная регистрация'