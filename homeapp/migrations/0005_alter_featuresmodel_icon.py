# Generated by Django 5.0.1 on 2024-02-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_image_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuresmodel',
            name='icon',
            field=models.CharField(default='fas fa-car-side fa-3x text-white', max_length=100),
        ),
    ]
