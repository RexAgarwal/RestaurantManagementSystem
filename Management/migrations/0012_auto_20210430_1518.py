# Generated by Django 3.0.8 on 2021-04-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0011_auto_20210429_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='designation',
            field=models.CharField(choices=[['Manager', 'Manager'], ['Cook', 'Cook'], ['Waitor', 'Waitor'], ['DeliveryBoy', 'DeliveryBoy']], max_length=50),
        ),
    ]
