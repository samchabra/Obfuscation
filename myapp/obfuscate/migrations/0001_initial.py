# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('obf_id', models.SlugField(serialize=False, max_length=32, primary_key=True)),
                ('target', models.URLField()),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
