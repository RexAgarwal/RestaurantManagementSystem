# Generated by Django 3.0.8 on 2021-05-01 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0016_auto_20210501_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_menu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Management.Menu'),
        ),
    ]
