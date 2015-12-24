# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJprojectapp', '0006_auto_20151222_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='list',
        ),
        migrations.DeleteModel(
            name='contest',
        ),
    ]
