# Generated by Django 3.0.2 on 2020-06-03 09:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0005_auto_20200513_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='MarketRating',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='TechRating',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
