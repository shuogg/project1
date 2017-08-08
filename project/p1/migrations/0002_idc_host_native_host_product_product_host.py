# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-07 09:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idc_Host',
            fields=[
                ('idc_name', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('lan_ip', models.CharField(max_length=16, null=True)),
                ('wan_ip', models.CharField(max_length=16, null=True)),
                ('type', models.IntegerField(null=True)),
                ('cpu_type', models.CharField(max_length=30, null=True)),
                ('cpu_number', models.IntegerField(null=True)),
                ('memory_size', models.CharField(max_length=20, null=True)),
                ('disk_size', models.CharField(max_length=20, null=True)),
                ('disk_type', models.CharField(max_length=20, null=True)),
                ('create_time', models.DateField()),
            ],
            options={
                'db_table': 'Idc_Host',
            },
        ),
        migrations.CreateModel(
            name='Native_Host',
            fields=[
                ('idc_name', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('lan_ip', models.CharField(max_length=16, null=True)),
                ('wan_ip', models.CharField(max_length=16, null=True)),
                ('Cabinet', models.CharField(max_length=30, null=True)),
                ('type', models.IntegerField(null=True)),
                ('cpu_type', models.CharField(max_length=30, null=True)),
                ('cpu_number', models.IntegerField(null=True)),
                ('memory_size', models.CharField(max_length=20, null=True)),
                ('disk_size', models.CharField(max_length=20, null=True)),
                ('disk_type', models.CharField(max_length=20, null=True)),
                ('create_time', models.DateField()),
            ],
            options={
                'db_table': 'Native_Host',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=30)),
                ('create_time', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Product_Host',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('lan_ip', models.CharField(max_length=16, null=True)),
                ('wan_ip', models.CharField(max_length=16, null=True)),
                ('hid', models.CharField(max_length=30, null=True)),
                ('type', models.IntegerField(null=True)),
                ('cpu_type', models.CharField(max_length=30, null=True)),
                ('cpu_number', models.IntegerField(null=True)),
                ('memory_size', models.CharField(max_length=20, null=True)),
                ('disk_size', models.CharField(max_length=20, null=True)),
                ('disk_type', models.CharField(max_length=20, null=True)),
                ('create_time', models.DateField()),
                ('native_host', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'Product_Host',
            },
        ),
    ]
