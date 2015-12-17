# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJ2app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userID', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('problemID', models.CharField(max_length=15)),
                ('problemTitle', models.CharField(max_length=35)),
                ('speak', models.TextField(max_length=300)),
            ],
        ),
    ]
