# Generated by Django 3.0.8 on 2021-05-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0033_auto_20210502_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount_paid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tax',
            field=models.FloatField(),
        ),
    ]
