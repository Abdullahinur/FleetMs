# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 11:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owner', '0001_initial'),
        ('sacco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignCrew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(default='/static/img/placeholder.png', upload_to='profile_pictures/conductor')),
                ('sacco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sacco.Sacco')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('id_number', models.IntegerField(unique=True)),
                ('profile_picture', models.ImageField(default='/static/img/placeholder.png', upload_to='profile_pictures/driver')),
                ('sacco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sacco.Sacco')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(null=True, unique=True)),
                ('mobile_phone_number', models.IntegerField(null=True)),
                ('profile_picture', models.ImageField(default='/static/img/placeholder.png', upload_to='profile_pictures/supervisor')),
                ('sacco_base', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sacco_base', to='sacco.Sacco')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='supervisor.Supervisor'),
        ),
        migrations.AddField(
            model_name='message',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='supervisor.Issue'),
        ),
        migrations.AddField(
            model_name='message',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='supervisor.Supervisor'),
        ),
        migrations.AddField(
            model_name='issue',
            name='supervisor_started',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor_started', to='supervisor.Supervisor'),
        ),
        migrations.AddField(
            model_name='assigncrew',
            name='conductor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supervisor.Conductor'),
        ),
        migrations.AddField(
            model_name='assigncrew',
            name='driver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supervisor.Driver'),
        ),
        migrations.AddField(
            model_name='assigncrew',
            name='vehicle_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.Vehicle'),
        ),
    ]