# Generated by Django 4.2.5 on 2023-09-23 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.TextField(max_length=20)),
                ('Adress', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20)),
                ('relagion', models.CharField(choices=[('Hindu', 'Hindu'), ('Muslim', 'Muslim'), ('Buddha', 'Buddha'), ('Christan', 'Christan')], max_length=20)),
            ],
        ),
    ]