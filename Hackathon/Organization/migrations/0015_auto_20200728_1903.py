# Generated by Django 3.0.2 on 2020-07-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0014_auto_20200719_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=200),
        ),
    ]
