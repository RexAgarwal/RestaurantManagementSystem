# Generated by Django 3.0.8 on 2021-05-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0025_auto_20210501_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]