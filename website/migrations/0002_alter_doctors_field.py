# Generated by Django 4.0.2 on 2022-02-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='Field',
            field=models.CharField(choices=[('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Cardiologists', 'Cardiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'), ('Critical Care Medicine Specialists', 'Critical Care Medicine Specialists'), ('Dermatologists', 'Dermatologists'), ('Endocrinologists', 'Endocrinologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Family Physicians', 'Family Physicians'), ('Gastroenterologists', 'Gastroenterologists'), ('Geriatric Medicine Specialists', 'Geriatric Medicine Specialists'), ('Hematologists', 'Hematologists'), ('Hospice and Palliative Medicine Specialists', 'Hospice and Palliative Medicine Specialists'), ('Infectious Disease Specialists', 'Infectious Disease Specialists'), ('Internists', 'Internists'), ('Medical Geneticists', 'Medical Geneticists'), ('Nephrologists', 'Nephrologists'), ('Obstetricians and Gynecologists', 'Obstetricians and Gynecologists'), ('Oncologists', 'Oncologists'), ('Ophthalmologists', 'Ophthalmologists')], max_length=256),
        ),
    ]
