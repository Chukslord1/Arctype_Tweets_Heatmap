# Generated by Django 3.1.7 on 2021-06-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20210622_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='created_at',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tweets',
            name='username',
            field=models.TextField(),
        ),
    ]