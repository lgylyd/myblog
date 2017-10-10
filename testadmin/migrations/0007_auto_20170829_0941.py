# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testadmin', '0006_auto_20170807_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseinfo',
            name='modify_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='databaseinfo',
            name='modify_user',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe4\xba\xba'),
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='modify_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='modify_user',
            field=models.CharField(default=b'', max_length=10, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe4\xba\xba'),
        ),
    ]
