# Generated by Django 3.0.8 on 2021-05-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0019_auto_20210501_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='building_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
