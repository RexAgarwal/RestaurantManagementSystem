# Generated by Django 3.0.8 on 2021-05-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0028_auto_20210501_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
