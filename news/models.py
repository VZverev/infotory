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
    short_text = models.TextField(u'Анотация', max_length = 1000, blank=True)
    causer = models.TextField(u'Виновник', max_length = 1000, blank=True)
    place = models.CharField(u'Место проведения', max_length=40, blank=True)
    analysis = models.TextField(u'Анализ', max_length = 1000, blank=True)
    
    votes_count = models.IntegerField(default=0)
    votes_sum = models.IntegerField(default=0)
    
    author = models.ForeignKey(User, verbose_name=u'Автор', blank=True, null=True) 
    image = models.ManyToManyField(Image, verbose_name=u'Изображения', blank=True, related_name='articles')
    tag = models.ManyToManyField(Tag, verbose_name=u'Тэги', blank=True, related_name='articles')
    file = models.ManyToManyField(File, verbose_name=u'Файлы', blank=True, related_name='articles')
    
    event = models.ForeignKey(Event, verbose_name=u'Событие', blank=True, null=True)
    
    class Meta():
        db_table = 'news_articles'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering=['pub_date']
        
    def __unicode__(self):
        return self.title
    
    def show_author(self):
        if self.author:
            return self.author.username
        else:
            return ''
    
    def show_author(self):
        if self.author:
            return self.author.username
        else:
            return ''
    show_author.short_description = u'Автор'
        
    def get_raiting(self):
        if self.votes_count and self.votes_sum:
            return 10.0*self.votes_sum/self.votes_count
        else:
            return 0
        
    get_raiting.short_description = u'Рейтинг'
        
    def show_tags(self):
        if self.tag:
            return "\n".join([t.title for t in self.tag.all()])
        else:
            return ''
    show_tags.short_description = u'Тэги'
    
class Comment(models.Model):
    record = models.ForeignKey(Article, verbose_name=u'Новость', blank=True, null=True, related_name='comments')
    pub_date = models.DateTimeField(u'Дата публикации', default=datetime.now)
    title = models.CharField(u'Заголовок', max_length = 40)
    text = models.TextField(u'Текст')
    author = models.ForeignKey(User, verbose_name=u'Автор', blank=True, null=True) 
    
    class Meta():
        db_table = 'news_comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering=['pub_date']
        
    def __unicode__(self):
        return self.title
    
    def show_author(self):
        if self.author:
            return self.author.username
        else:
            return ''
    show_author.short_description = u'Автор'
    
    def show_short_text(self):
        return self.text[:200]
    show_short_text.short_description = u'Автор'
    
    