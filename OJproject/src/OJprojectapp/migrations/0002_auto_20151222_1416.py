# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OJprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemslist',
            name='mem_limit',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='problemslist',
            name='time_limit',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_status',
            name='memory',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_status',
            name='problemID',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user_status',
            name='problemSID',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user_status',
            name='time',
            field=models.CharField(max_length=30),
        ),
    ]
