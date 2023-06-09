# Generated by Django 4.1.6 on 2023-02-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mail',
        ),
        migrations.AddField(
            model_name='patient',
            name='date_de_naissaince',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='emploi',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='groupe_sanguin',
            field=models.CharField(choices=[('O', 'O'), ('A', 'A'), ('B', 'B'), ('AB', 'AB')], default='O', max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='photo',
            field=models.ImageField(blank=True, upload_to='patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='telephone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], default='M', max_length=10),
        ),
    ]
