# Generated by Django 2.2.8 on 2020-01-21 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_text', models.CharField(max_length=100)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain', to='quiz.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Technology', models.PositiveIntegerField(null=True)),
                ('Marketing', models.PositiveIntegerField(null=True)),
                ('Total', models.PositiveIntegerField(null=True)),
                ('Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_domain', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DomainQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_text', models.CharField(max_length=100)),
                ('Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_specific', to='quiz.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='DomainMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.PositiveIntegerField(null=True)),
                ('Domain_final', models.CharField(max_length=25)),
                ('Name_of_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='for_final_marks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DomainAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weightage', models.PositiveIntegerField()),
                ('Answer_text', models.CharField(max_length=255)),
                ('Question_related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question_domain', to='quiz.DomainQuestion')),
                ('from_Domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_domain_in_specific', to='quiz.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weightage', models.PositiveIntegerField()),
                ('Answer_text', models.CharField(max_length=255)),
                ('Question_related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question', to='quiz.Question')),
                ('from_Domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_domain', to='quiz.Domain')),
            ],
        ),
    ]
