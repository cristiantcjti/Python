# Generated by Django 2.1.15 on 2021-05-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='rg',
            field=models.CharField(max_length=9),
        ),
    ]
