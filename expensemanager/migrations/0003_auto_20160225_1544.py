# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanager', '0002_auto_20160225_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='userid',
            field=models.IntegerField(blank=True),
        ),
    ]
