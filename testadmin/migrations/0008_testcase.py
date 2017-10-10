# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testadmin', '0007_auto_20170829_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe4\xbe\x8b\xe7\xbc\x96\xe5\x8f\xb7')),
                ('function_model', models.CharField(max_length=200, verbose_name=b'\xe5\x8a\x9f\xe8\x83\xbd\xe6\xa8\xa1\xe5\x9d\x97')),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('precondition', models.TextField(verbose_name=b'\xe5\x89\x8d\xe7\xbd\xae\xe6\x9d\xa1\xe4\xbb\xb6')),
                ('procedure', models.TextField(verbose_name=b'\xe6\xb5\x8b\xe8\xaf\x95\xe6\xad\xa5\xe9\xaa\xa4')),
                ('ex_result', models.TextField(verbose_name=b'\xe9\xa2\x84\xe6\x9c\x9f\xe7\xbb\x93\xe6\x9e\x9c')),
                ('pr_result', models.TextField(verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe7\xbb\x93\xe6\x9e\x9c')),
                ('test_result', models.CharField(max_length=5, verbose_name=b'\xe6\xb5\x8b\xe8\xaf\x95\xe7\xbb\x93\xe6\x9e\x9c')),
                ('grade', models.CharField(max_length=5, verbose_name=b'\xe7\x94\xa8\xe4\xbe\x8b\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7')),
            ],
        ),
    ]
