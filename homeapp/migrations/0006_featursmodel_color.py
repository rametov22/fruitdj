# Generated by Django 5.0.1 on 2024-02-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_alter_featuresmodel_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='featursmodel',
            name='color',
            field=models.CharField(default='service-item bg-secondary rounded border border-secondary', max_length=100),
        ),
    ]
