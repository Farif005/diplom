# Generated by Django 4.2 on 2024-05-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='image',
            field=models.ImageField(default='fef', upload_to='images/', verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
