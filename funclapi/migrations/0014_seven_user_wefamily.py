# Generated by Django 2.2.2 on 2020-10-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funclapi', '0013_auto_20201005_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='seven',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100)),
                ('calories', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('bmr', models.CharField(max_length=100)),
                ('tdee', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='wefamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100)),
                ('perserving', models.CharField(max_length=100)),
                ('calories', models.CharField(max_length=100)),
                ('protein', models.CharField(max_length=100)),
                ('fat', models.CharField(max_length=100)),
                ('saturatedfat', models.CharField(max_length=100)),
                ('transfat', models.CharField(max_length=100)),
                ('carbohydrate', models.CharField(max_length=100)),
                ('sodium', models.CharField(max_length=100)),
                ('sugar', models.CharField(max_length=100)),
                ('picture', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
