# Generated by Django 3.1.7 on 2021-06-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20210611_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='username',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
