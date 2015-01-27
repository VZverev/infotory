# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import resources.models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('file', models.FileField(upload_to=resources.models.upload_file, verbose_name='\u0424\u0430\u0439\u043b')),
                ('desc_short', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('tag', models.ManyToManyField(to='tags.Tag', null=True, verbose_name=b'\xd0\xa2\xd1\x8d\xd0\xb3', blank=True)),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'resources_file',
                'verbose_name': '\u0424\u0430\u0439\u043b',
                'verbose_name_plural': '\u0424\u0430\u0439\u043b\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('desc_short', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('file', models.ImageField(upload_to=resources.models.upload_image, verbose_name='\u0424\u0430\u0439\u043b')),
                ('tag', models.ManyToManyField(to='tags.Tag', null=True, verbose_name=b'\xd0\xa2\xd1\x8d\xd0\xb3', blank=True)),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'resources_image',
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
    ]
