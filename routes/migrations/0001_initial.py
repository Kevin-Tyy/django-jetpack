# Generated by Django 5.1.2 on 2024-10-23 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0002_vehicle_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location', models.CharField(max_length=100)),
                ('end_location', models.CharField(max_length=100)),
                ('estimated_travel_time', models.DurationField()),
                ('distance', models.FloatField(help_text='Distance in kilometers')),
                ('route_name', models.CharField(max_length=100, unique=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('vehicles', models.ManyToManyField(blank=True, related_name='routes', to='vehicles.vehicle')),
            ],
        ),
    ]
