# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'tags_tag',
                'verbose_name': '\u0422\u044d\u0433',
                'verbose_name_plural': '\u0422\u044d\u0433\u0438',
            },
            bases=(models.Model,),
        ),
    ]
