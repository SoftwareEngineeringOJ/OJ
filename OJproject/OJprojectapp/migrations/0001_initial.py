# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groupdetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(max_length=50)),
                ('sumrank', models.CharField(max_length=50)),
                ('competedate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HOJ_Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('problem', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('dificulty', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NOJ_Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('problem', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('dificulty', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='POJ_Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('problem', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('dificulty', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('statu', models.CharField(max_length=10)),
                ('submittime', models.DateTimeField()),
                ('runningtime', models.CharField(max_length=10)),
                ('memory', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TYVJ_Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('problem', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('dificulty', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('precision', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('algorithm', models.CharField(max_length=10)),
                ('speed', models.CharField(max_length=10)),
                ('sumrank', models.CharField(max_length=50)),
                ('HOJ', models.ManyToManyField(to='OJprojectapp.HOJ_Problems')),
                ('NOJ', models.ManyToManyField(to='OJprojectapp.NOJ_Problems')),
                ('POJ', models.ManyToManyField(to='OJprojectapp.POJ_Problems')),
                ('TYVJ', models.ManyToManyField(to='OJprojectapp.TYVJ_Problems')),
            ],
        ),
        migrations.CreateModel(
            name='ZOJ_Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('problem', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('dificulty', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='userdetail',
            name='ZOJ',
            field=models.ManyToManyField(to='OJprojectapp.ZOJ_Problems'),
        ),
    ]
