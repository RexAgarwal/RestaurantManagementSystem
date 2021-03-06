# Generated by Django 3.0.8 on 2021-04-29 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0007_order_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menu',
        ),
        migrations.CreateModel(
            name='Order_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Management.Menu')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Management.Order')),
            ],
        ),
    ]
