# Generated by Django 3.0.8 on 2021-04-29 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0009_auto_20210429_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_menu',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.Order'),
        ),
    ]
