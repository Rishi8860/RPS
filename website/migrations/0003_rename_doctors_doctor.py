# Generated by Django 4.0.2 on 2022-02-12 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_doctors_field'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
    ]