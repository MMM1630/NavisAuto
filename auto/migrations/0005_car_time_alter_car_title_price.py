# Generated by Django 5.2 on 2025-04-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_remove_car_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='time',
            field=models.CharField(default=1, max_length=20, verbose_name='Срок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='title_price',
            field=models.CharField(max_length=20, verbose_name='Ежемесячный платеж'),
        ),
    ]
