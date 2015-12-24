# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJprojectapp', '0007_auto_20151223_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest_tmp',
            name='list',
        ),
        migrations.DeleteModel(
            name='contest_tmp',
        ),
    ]
