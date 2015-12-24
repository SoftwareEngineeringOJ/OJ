# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJprojectapp', '0008_auto_20151223_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='contest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('announcement', models.TextField()),
                ('password', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('begintime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('IsReady', models.BooleanField()),
                ('list', models.ManyToManyField(to='OJprojectapp.contest_problem')),
            ],
        ),
    ]
