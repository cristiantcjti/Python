# Generated by Django 2.1.15 on 2021-05-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210505_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='medical_insurance',
            field=models.CharField(max_length=70),
        ),
    ]
