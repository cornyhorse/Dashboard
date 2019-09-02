# Generated by Django 2.2.4 on 2019-09-01 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputeResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portable', models.BooleanField(blank=True, null=True)),
                ('local_ipv4_address', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('local_ipv6_address', models.GenericIPAddressField(blank=True, null=True, protocol='IPv6')),
                ('external_ipv4_address', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('external_ipv6_address', models.GenericIPAddressField(blank=True, null=True, protocol='IPv6')),
                ('powered_on', models.BooleanField(blank=True, null=True)),
                ('powered_on_utc', models.DateTimeField(blank=True, null=True)),
                ('uptime', models.DurationField(blank=True, null=True)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComputeSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compute.ComputeResource')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=15)),
                ('computesensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compute.ComputeSensor')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_name', models.CharField(max_length=255)),
                ('network_description', models.TextField(blank=True, null=True)),
                ('located_in_cloud', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=255)),
                ('adapter_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SensorHeartbeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heartbeat_utc', models.DateTimeField()),
                ('raw', models.TextField()),
                ('compute_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compute.ComputeSensor')),
            ],
        ),
        migrations.CreateModel(
            name='SensorMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, max_digits=10)),
                ('heartbeat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compute.SensorHeartbeat')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compute.Measurement')),
            ],
        ),
        migrations.AddField(
            model_name='computesensor',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compute.Sensor'),
        ),
        migrations.AddField(
            model_name='computeresource',
            name='network',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='compute.Network'),
        ),
        migrations.AddField(
            model_name='computeresource',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
