# Generated by Django 5.0.1 on 2024-02-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0010_productmodel_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomments',
            name='stars',
            field=models.IntegerField(default=0, verbose_name='оценка'),
        ),
    ]
