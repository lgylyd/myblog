# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testadmin', '0003_auto_20170804_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe5\xad\x97')),
                ('address', models.URLField(max_length=100, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('account', models.CharField(max_length=20, verbose_name=b'\xe8\xb4\xa6\xe5\x8f\xb7')),
                ('password', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('database_name', models.CharField(max_length=20, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93\xe5\x90\x8d\xe5\xad\x97')),
                ('create_user', models.CharField(max_length=10, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe4\xba\xba')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
