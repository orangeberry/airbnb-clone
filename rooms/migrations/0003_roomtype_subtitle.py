# Generated by Django 3.1.4 on 2021-01-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20210107_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='subtitle',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
