# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJprojectapp', '0003_contest_ext'),
    ]

    operations = [
        migrations.CreateModel(
            name='contest_problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titles', models.CharField(max_length=50)),
                ('pids', models.CharField(max_length=15)),
                ('sojs', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='contest_ext',
        ),
        migrations.RemoveField(
            model_name='contest_tmp',
            name='count',
        ),
        migrations.AddField(
            model_name='contest',
            name='list',
            field=models.ManyToManyField(to='OJprojectapp.contest_problem'),
        ),
        migrations.AddField(
            model_name='contest_tmp',
            name='list',
            field=models.ManyToManyField(to='OJprojectapp.contest_problem'),
        ),
    ]
