# Generated by Django 3.0.8 on 2021-05-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0030_remove_order_menu_times_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='building_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
