# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testadmin', '0009_auto_20170829_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='project_name',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d'),
        ),
    ]
