# Generated by Django 3.0.8 on 2021-05-02 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0029_auto_20210502_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_menu',
            name='times_ordered',
        ),
    ]
