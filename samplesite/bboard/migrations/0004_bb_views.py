# Generated by Django 4.2 on 2024-05-23 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
