# Generated by Django 2.2.1 on 2019-06-21 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0013_auto_20190622_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicleexit',
            old_name='tagno',
            new_name='tno',
        ),
        migrations.RenameField(
            model_name='vehicleexit',
            old_name='vnumber',
            new_name='vno',
        ),
        migrations.RenameField(
            model_name='vehicleexit',
            old_name='vtype',
            new_name='vtypee',
        ),
    ]