# Generated by Django 3.0.8 on 2021-04-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0003_auto_20210426_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
