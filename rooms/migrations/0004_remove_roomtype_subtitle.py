# Generated by Django 3.1.4 on 2021-01-06 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_roomtype_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtype',
            name='subtitle',
        ),
    ]
