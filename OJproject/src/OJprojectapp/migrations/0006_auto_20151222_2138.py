# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJprojectapp', '0005_auto_20151222_2136'),
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
            ],
        ),
        migrations.CreateModel(
            name='contest_problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titles', models.CharField(max_length=50)),
                ('pids', models.CharField(max_length=15)),
                ('sojs', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='contest_tmp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('announcement', models.TextField()),
                ('password', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('begintime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('list', models.ManyToManyField(to='OJprojectapp.contest_problem')),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='list',
            field=models.ManyToManyField(to='OJprojectapp.contest_problem'),
        ),
    ]
