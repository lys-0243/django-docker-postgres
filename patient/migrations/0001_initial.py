# Generated by Django 4.1.6 on 2023-02-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('prenom', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('sexe', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10)),
            ],
        ),
    ]
