# Generated by Django 4.1.3 on 2022-11-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=15, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('channel', models.CharField(max_length=30)),
                ('published_at', models.DateTimeField()),
                ('thumbnail_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='YouTubeAPIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=40, unique=True)),
            ],
        ),
    ]