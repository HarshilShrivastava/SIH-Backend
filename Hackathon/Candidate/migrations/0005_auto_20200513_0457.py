# Generated by Django 3.0.2 on 2020-05-13 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0004_auto_20200507_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainmark',
            name='Recruit2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_profile', to='Candidate.Recruit'),
        ),
        migrations.AlterField(
            model_name='subdomainmark',
            name='Recruit3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to='Candidate.Recruit'),
        ),
    ]
