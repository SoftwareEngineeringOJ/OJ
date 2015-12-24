# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJprojectapp', '0004_auto_20151222_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='list',
        ),
        migrations.RemoveField(
            model_name='contest_tmp',
            name='list',
        ),
        migrations.DeleteModel(
            name='contest',
        ),
        migrations.DeleteModel(
            name='contest_problem',
        ),
        migrations.DeleteModel(
            name='contest_tmp',
        ),
    ]
