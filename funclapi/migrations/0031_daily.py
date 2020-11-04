# Generated by Django 2.2.2 on 2020-11-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funclapi', '0030_eat'),
    ]

    operations = [
        migrations.CreateModel(
            name='daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
