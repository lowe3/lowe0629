# Generated by Django 2.2.2 on 2020-06-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
