# Generated by Django 3.0.8 on 2021-05-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0034_auto_20210502_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
