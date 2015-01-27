# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('start_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430')),
                ('end_date', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0446\u0430')),
                ('desc_short', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('desc_full', models.TextField(verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('place', models.CharField(max_length=40, verbose_name='\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f', blank=True)),
                ('duration', models.FloatField(null=True, verbose_name='\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c', blank=True)),
                ('image', models.ManyToManyField(related_name='events', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f', to='resources.Image', blank=True)),
                ('info', models.ManyToManyField(related_name='events', verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f', to='resources.File', blank=True)),
                ('tag', models.ManyToManyField(related_name='events', verbose_name='\u0422\u044d\u0433\u0438', to='tags.Tag', blank=True)),
            ],
            options={
                'ordering': ['title'],
                'db_table': 'events_event',
                'verbose_name': '\u0421\u043e\u0431\u044b\u0442\u0438\u0435',
                'verbose_name_plural': '\u0421\u043e\u0431\u044b\u0442\u0438\u044f',
            },
            bases=(models.Model,),
        ),
    ]
