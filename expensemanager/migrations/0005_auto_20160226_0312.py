# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanager', '0004_auto_20160225_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='public',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(),
        ),
    ]
