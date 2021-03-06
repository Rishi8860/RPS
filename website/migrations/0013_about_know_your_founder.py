# Generated by Django 4.0.2 on 2022-04-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_doctor_name_hindi_field_field_hindi'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About_us', models.TextField()),
                ('Front_page_photo', models.ImageField(upload_to='Front_page_photo/')),
            ],
        ),
        migrations.CreateModel(
            name='Know_Your_Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256, unique=True)),
                ('Photo', models.ImageField(upload_to='Founder_photo/')),
                ('About', models.TextField()),
            ],
        ),
    ]
