# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userID', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('problemID', models.CharField(max_length=15)),
                ('problemTitle', models.CharField(max_length=35)),
                ('speak', models.TextField(max_length=300)),
                ('like', models.TextField(max_length=50)),
                ('dislike', models.TextField(max_length=50)),
                ('submit_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=50)),
                ('register_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='group_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupID', models.CharField(max_length=30)),
                ('groupname', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
                ('competedate', models.DateTimeField()),
                ('codes', models.TextField()),
                ('is_codes_private', models.BooleanField()),
                ('is_group_private', models.BooleanField()),
                ('submit_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='problemslist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('OJ', models.CharField(max_length=20)),
                ('SID', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('ratio', models.CharField(max_length=50)),
                ('time_limit', models.CharField(max_length=15)),
                ('mem_limit', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('inputs', models.TextField()),
                ('output', models.TextField()),
                ('sample_input', models.TextField()),
                ('sample_output', models.TextField()),
                ('hint', models.TextField()),
                ('pic', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('signature', models.TextField(max_length=200)),
                ('school', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('register_time', models.DateTimeField()),
                ('answered', models.CharField(max_length=50)),
                ('wrong', models.CharField(max_length=50)),
                ('right', models.CharField(max_length=50)),
                ('contest_number', models.CharField(max_length=50)),
                ('contest_wrong', models.CharField(max_length=50)),
                ('contest_right', models.CharField(max_length=50)),
                ('contests', models.ManyToManyField(to='OJprojectapp.group_status')),
            ],
        ),
        migrations.CreateModel(
            name='user_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problemID', models.CharField(max_length=15)),
                ('problemTitle', models.CharField(max_length=35)),
                ('problemSID', models.CharField(max_length=15)),
                ('contestID', models.CharField(max_length=10)),
                ('userID', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('OJ', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=30)),
                ('memory', models.CharField(max_length=15)),
                ('time', models.CharField(max_length=15)),
                ('language', models.CharField(max_length=10)),
                ('code', models.TextField()),
                ('submit_time', models.DateTimeField()),
                ('is_code_private', models.BooleanField()),
                ('is_user_private', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='problems',
            field=models.ManyToManyField(to='OJprojectapp.user_status'),
        ),
        migrations.AddField(
            model_name='group',
            name='groupmembers',
            field=models.ManyToManyField(to='OJprojectapp.user'),
        ),
    ]
