# Generated by Django 3.0.2 on 2020-07-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0017_auto_20200708_2012'),
        ('content', '0003_auto_20200630_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('By', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='courses')),
                ('Refrences', models.URLField(max_length=255)),
                ('Apply', models.URLField(max_length=255)),
                ('SocialMediaTags', models.ManyToManyField(blank=True, to='Candidate.SocialMediaTags')),
                ('SocioeconomicTags', models.ManyToManyField(blank=True, to='Candidate.SocioeconomicTags')),
            ],
        ),
    ]
