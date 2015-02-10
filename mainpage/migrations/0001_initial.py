# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('image', models.FileField(upload_to=b'', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('text', models.CharField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maintext', models.CharField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True)),
                ('maintext1', models.CharField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442 (1)', blank=True)),
                ('footertext', models.CharField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434\u0432\u0430\u043b (footer)', blank=True)),
                ('contacttext', models.CharField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043a\u043e\u043d\u0442\u0430\u043a\u0442 (contact)', blank=True)),
                ('freetext', models.CharField(max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u0442 (free)', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
