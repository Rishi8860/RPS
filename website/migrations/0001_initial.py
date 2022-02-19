# Generated by Django 4.0.2 on 2022-02-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=256)),
                ('Field', models.CharField(max_length=256)),
                ('Photo', models.ImageField(upload_to='Doctors/')),
                ('About', models.TextField()),
            ],
        ),
    ]