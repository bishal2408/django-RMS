# Generated by Django 4.1 on 2022-08-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_orders_order_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_firstname',
            field=models.CharField(default='xyz', max_length=12),
        ),
    ]
