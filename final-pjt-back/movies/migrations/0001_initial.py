# Generated by Django 3.2.9 on 2021-11-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('adult', models.BooleanField(null=True)),
                ('backdrop_path', models.TextField(null=True)),
                ('genre_ids', models.TextField(null=True)),
                ('original_language', models.CharField(max_length=100, null=True)),
                ('original_title', models.TextField(null=True)),
                ('video', models.BooleanField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('release_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('adult', models.BooleanField(null=True)),
                ('backdrop_path', models.TextField(null=True)),
                ('genre_ids', models.TextField(null=True)),
                ('original_language', models.CharField(max_length=100, null=True)),
                ('original_title', models.TextField(null=True)),
                ('video', models.BooleanField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('release_date', models.DateField(null=True)),
            ],
        ),
    ]
