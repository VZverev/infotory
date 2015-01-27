# -*- coding: utf-8 -*- 
from django.db import models

from tags.models import Tag
from resources.models import Image, File


class Event(models.Model):
    title = models.CharField(u'Название', max_length = 40)
    start_date = models.DateTimeField(u'Дата начала')
    end_date = models.DateTimeField(u'Дата конца')
    desc_short = models.TextField(u'Краткое описание',blank=True)
    desc_full = models.TextField(u'Полное описание',blank=True)
    place = models.CharField(u'Место проведения', max_length=40, blank=True)
    duration = models.FloatField(u'Длительность',blank=True, null=True)
    
    infos = models.ManyToManyField(File, verbose_name=u'Информация', blank=True, related_name='events')
    tags = models.ManyToManyField(Tag, verbose_name=u'Тэги', blank=True, related_name='events')
    images = models.ManyToManyField(Image, verbose_name=u'Изображения', blank=True, related_name='events')
    
    class Meta():
        db_table = 'events_event'
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering=['title']
        
    def __unicode__(self):
        return self.title