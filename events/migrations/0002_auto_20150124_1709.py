# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='info',
            new_name='infos',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='tag',
            new_name='tags',
        ),
    ]
