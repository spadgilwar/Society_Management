# Generated by Django 2.2.3 on 2019-10-22 20:21

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('property', '0006_property_services'),
        ('resident_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Risident_info',
            new_name='Resident_info',
        ),
    ]