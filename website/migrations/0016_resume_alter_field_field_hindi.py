# Generated by Django 4.0.2 on 2022-06-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_doctor_name_hindi_alter_field_field_hindi'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('Contact', models.CharField(max_length=256)),
                ('Sub', models.CharField(max_length=256)),
                ('Email', models.CharField(max_length=256)),
                ('Message', models.CharField(max_length=256)),
                ('Resume', models.FileField(upload_to='Resume/')),
            ],
        ),
        migrations.AlterField(
            model_name='field',
            name='Field_Hindi',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]