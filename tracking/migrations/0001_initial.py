# Generated by Django 4.0 on 2024-08-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracker_id', models.CharField(max_length=50, unique=True)),
                ('tracking_number', models.CharField(max_length=50)),
            ],
        ),
    ]
