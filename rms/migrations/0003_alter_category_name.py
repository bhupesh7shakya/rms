# Generated by Django 4.2.5 on 2023-09-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0002_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]