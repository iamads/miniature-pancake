# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanager', '0003_auto_20160225_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='userid',
            field=models.IntegerField(),
        ),
    ]
