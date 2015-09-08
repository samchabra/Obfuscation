# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obfuscate', '0002_auto_20150907_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='obf_id',
            field=models.SlugField(max_length=32, primary_key=True, serialize=False),
        ),
    ]
