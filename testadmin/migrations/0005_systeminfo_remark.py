# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testadmin', '0004_systeminfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='systeminfo',
            name='remark',
            field=models.TextField(default=1, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8'),
            preserve_default=False,
        ),
    ]
