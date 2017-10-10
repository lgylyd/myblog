# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testadmin', '0005_systeminfo_remark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systeminfo',
            name='database_name',
        ),
        migrations.AddField(
            model_name='systeminfo',
            name='database_name',
            field=models.ManyToManyField(to='testadmin.DatabaseInfo', verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93', blank=True),
        ),
    ]
