# Generated by Django 5.1.3 on 2024-12-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_syncbomlist_itemdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropdownfield',
            name='readMore',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]