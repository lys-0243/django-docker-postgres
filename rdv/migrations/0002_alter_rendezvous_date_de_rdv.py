# Generated by Django 4.1.6 on 2023-02-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendezvous',
            name='date_de_rdv',
            field=models.DateField(),
        ),
    ]