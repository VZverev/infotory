# -*- coding: utf-8 -*- 
from datetime import datetime  
from django.db import models
from django.contrib.auth.models import User
from events.models import Event
from tags.models import Tag
from resources.models import Image, File

class Article(models.Model):
    pub_date = models.DateTimeField(u'Дата публикации', default=datetime.now)
    title = models.CharField(u'Заголовок', max_length = 40)
    full_text = models.TextField(u'Текст')
    annotation = models.TextField(u'Анотация', max_length = 1000, blank=True)
    causer = models.TextField(u'Виновник', max_length = 1000, blank=True)
    place = models.CharField(u'Место проведения', max_length=40, blank=True)
    analysis = models.TextField(u'Анализ', max_length = 1000, blank=True)
    
    votes_count = models.IntegerField(default=0)
    votes_sum = models.IntegerField(default=0)
    
    publisher = models.ForeignKey(User, verbose_name=u'Автор', blank=True, null=True) 
    images = models.ManyToManyField(Image, verbose_name=u'Изображения', blank=True, related_name='articles')
    tags = models.ManyToManyField(Tag, verbose_name=u'Тэги', blank=True, related_name='articles')
    files = models.ManyToManyField(File, verbose_name=u'Файлы', blank=True, related_name='articles')
    
    class Meta():
        db_table = 'news_articles'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering=['pub_date']
        
    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    pub_date = models.DateTimeField(u'Дата публикации', default=datetime.now)
    title = models.CharField(u'Заголовок', max_length = 40)
    text = models.TextField(u'Текст')
    publisher = models.ForeignKey(User, verbose_name=u'Автор', blank=True, null=True) 
    
    class Meta():
        db_table = 'news_comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering=['pub_date']
        
    def __unicode__(self):
        return self.title
    
    