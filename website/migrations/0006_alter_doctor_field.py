# Generated by Django 4.0.2 on 2022-02-12 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_a_field_rename_b_field_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.field'),
        ),
    ]
