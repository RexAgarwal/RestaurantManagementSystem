# Generated by Django 3.0.8 on 2021-04-29 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_auto_20210429_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transc', to='Management.Order'),
        ),
    ]