# Generated by Django 3.1.7 on 2021-06-16 03:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20210615_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='time',
            field=models.TextField(default=datetime.datetime(2021, 6, 16, 3, 31, 2, 119115, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
