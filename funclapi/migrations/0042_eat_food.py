# Generated by Django 2.2.2 on 2020-11-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funclapi', '0041_auto_20201117_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='eat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('bmr', models.CharField(max_length=100)),
                ('tdee', models.CharField(max_length=100)),
                ('datetime', models.CharField(max_length=100)),
                ('items', models.CharField(max_length=250)),
                ('calories', models.FloatField()),
                ('total', models.FloatField()),
                ('times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=250)),
                ('calories', models.FloatField()),
                ('picture', models.CharField(max_length=250, null=True)),
                ('convenience', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
            ],
        ),
    ]
