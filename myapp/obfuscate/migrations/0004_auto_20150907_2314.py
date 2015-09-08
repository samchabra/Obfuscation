# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obfuscate', '0003_auto_20150907_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='obf_id',
            field=models.SlugField(serialize=False, max_length=36, primary_key=True),
        ),
    ]
