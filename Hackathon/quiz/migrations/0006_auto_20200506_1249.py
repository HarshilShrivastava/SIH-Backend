# Generated by Django 3.0.2 on 2020-05-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200505_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Question_text',
            field=models.TextField(),
        ),
    ]
