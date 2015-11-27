# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='groupdetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=50)),
                ('sumrank', models.CharField(max_length=50)),
                ('competedate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problemID', models.CharField(max_length=15)),
                ('OJ', models.CharField(max_length=20)),
                ('SID', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('time_limit', models.CharField(max_length=15)),
                ('mem_limit', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('inputs', models.TextField()),
                ('output', models.TextField()),
                ('sample_input', models.TextField()),
                ('sample_output', models.TextField()),
                ('hint', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='problemslist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problemID', models.CharField(max_length=15)),
                ('OJ', models.CharField(max_length=20)),
                ('SID', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('ratio', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('runID', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=30)),
                ('OJ', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=30)),
                ('memory', models.CharField(max_length=15)),
                ('time', models.CharField(max_length=15)),
                ('language', models.CharField(max_length=10)),
                ('code_file', models.CharField(max_length=50)),
                ('submit_time', models.DateTimeField()),
                ('userID', models.CharField(max_length=30)),
                ('contestID', models.CharField(max_length=10)),
                ('isprivate', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userID', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('signature', models.TextField(max_length=200)),
                ('school', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('register_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='userdetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('precision', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('algorithm', models.CharField(max_length=10)),
                ('speed', models.CharField(max_length=10)),
                ('sumrank', models.CharField(max_length=50)),
                ('problems', models.ManyToManyField(to='OJprojectapp.problems')),
            ],
        ),
    ]
