# Generated by Django 5.1.3 on 2024-12-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_ordernumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AlterField(
            model_name='order',
            name='orderNumber',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
