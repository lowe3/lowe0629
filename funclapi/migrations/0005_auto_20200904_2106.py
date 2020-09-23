# Generated by Django 2.2.2 on 2020-09-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funclapi', '0004_family_seven_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='wefamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=50)),
                ('perserving', models.CharField(max_length=50)),
                ('calories', models.CharField(max_length=50)),
                ('protein', models.CharField(max_length=50)),
                ('fat', models.CharField(max_length=50)),
                ('saturatedfat', models.CharField(max_length=50)),
                ('transfat', models.CharField(max_length=50)),
                ('carbohydrate', models.CharField(max_length=50)),
                ('sodium', models.CharField(max_length=50)),
                ('sugar', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='family',
        ),
    ]