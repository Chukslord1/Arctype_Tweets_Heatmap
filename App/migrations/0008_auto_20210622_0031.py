# Generated by Django 3.1.7 on 2021-06-21 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20210616_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='username',
            field=models.IntegerField(),
        ),
    ]