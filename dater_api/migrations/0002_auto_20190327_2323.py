# Generated by Django 2.1.5 on 2019-03-27 23:23

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('dater_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SlotTypes',
            new_name='SlotType',
        ),
    ]
