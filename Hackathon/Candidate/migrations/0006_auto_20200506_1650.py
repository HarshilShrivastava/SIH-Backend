# Generated by Django 3.0.2 on 2020-05-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0005_recruit_no_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='No_of',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
