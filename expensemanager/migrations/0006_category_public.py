# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanager', '0005_auto_20160226_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
