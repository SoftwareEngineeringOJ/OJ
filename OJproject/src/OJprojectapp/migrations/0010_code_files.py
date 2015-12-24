# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJprojectapp', '0009_contest'),
    ]

    operations = [
        migrations.CreateModel(
            name='code_files',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('runID', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=128)),
            ],
        ),
    ]
