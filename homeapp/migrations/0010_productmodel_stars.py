# Generated by Django 5.0.1 on 2024-02-27 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0009_reviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='stars',
            field=models.IntegerField(choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (5, '5 звезд')], default=4),
        ),
    ]
