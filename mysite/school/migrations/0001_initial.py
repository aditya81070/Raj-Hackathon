# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(default='Rajasthan', max_length=30)),
                ('City', models.CharField(choices=[('AJMER', 'Ajmer'), ('JAIPUR', 'Jaipur'), ('BANSWARA', 'Banswara'), ('AJMER', 'Ajmer')], default='AJMER', max_length=20)),
                ('Pin_Code', models.IntegerField()),
                ('School_Name', models.CharField(max_length=250)),
            ],
        ),
    ]
