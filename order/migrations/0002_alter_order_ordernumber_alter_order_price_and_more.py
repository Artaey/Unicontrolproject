# Generated by Django 5.1.3 on 2024-11-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='syncbomlist',
            name='no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='syncsparepart',
            name='price',
            field=models.IntegerField(),
        ),
    ]
