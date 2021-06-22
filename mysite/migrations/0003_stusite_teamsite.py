# Generated by Django 3.1.7 on 2021-06-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_city_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='StuSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('url', models.URLField()),
            ],
        ),
    ]