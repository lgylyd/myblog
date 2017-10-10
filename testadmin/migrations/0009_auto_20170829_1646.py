# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testadmin', '0008_testcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='create_user',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe4\xba\xba'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='modify_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='modify_user',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe4\xba\xba'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='status',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x88\xa0\xe9\x99\xa4'),
        ),
    ]
