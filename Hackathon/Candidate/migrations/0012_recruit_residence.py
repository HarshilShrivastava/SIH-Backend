# Generated by Django 3.0.2 on 2020-06-29 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0011_auto_20200629_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='Residence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Candidate.Residence'),
            preserve_default=False,
        ),
    ]
