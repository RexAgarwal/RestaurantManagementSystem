# Generated by Django 3.0.8 on 2021-04-26 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_auto_20210426_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='Management.Order'),
        ),
    ]