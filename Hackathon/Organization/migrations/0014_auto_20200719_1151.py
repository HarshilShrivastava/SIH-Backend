# Generated by Django 3.0.2 on 2020-07-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0013_jobs_subdomain'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillForJobs',
            fields=[
                ('Name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='jobs',
            name='Job_preprocess',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='SkillRequired',
            field=models.ManyToManyField(blank=True, to='Organization.SkillForJobs'),
        ),
    ]