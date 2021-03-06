# Generated by Django 4.0.2 on 2022-02-13 09:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_doctor_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header', models.CharField(max_length=256, unique=True)),
                ('Data', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='Joining',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 2, 13, 9, 9, 41, 356849, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='field',
            name='About',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='field',
            name='Field',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
