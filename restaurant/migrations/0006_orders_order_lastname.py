# Generated by Django 4.0.5 on 2022-08-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_orders_order_remove_orders_orderby_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_lastname',
            field=models.CharField(default='', max_length=12),
        ),
    ]
