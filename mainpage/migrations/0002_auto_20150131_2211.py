# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='text',
            field=models.TextField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textmodel',
            name='contacttext',
            field=models.TextField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043e\u043d\u0442\u0430\u043a\u0442 (contact)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textmodel',
            name='footertext',
            field=models.TextField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0432\u0430\u043b (footer)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textmodel',
            name='freetext',
            field=models.TextField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442 (free)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textmodel',
            name='maintext',
            field=models.TextField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textmodel',
            name='maintext1',
            field=models.TextField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442 (1)', blank=True),
            preserve_default=True,
        ),
    ]
