# Generated by Django 2.2 on 2019-04-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20190429_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
