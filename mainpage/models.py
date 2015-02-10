# -*- coding: utf-8 -*- 
from django.db import models

def short_text(text, len):
        return text[:len] + '...'
    
class ServiceModel(models.Model):
    title = models.CharField(u'Название', max_length=100)
    image = models.FileField(u'Картинка')
    text = models.TextField(u'Текст', max_length=50000)
    def short_text(self):
        return short_text(self.text, 50)
    
    def __unicode__(self):
        return self.title

class TextModel(models.Model):
    maintext = models.TextField(u'Текст', blank=True, max_length=50000)
    maintext1 = models.TextField(u'Текст (1)', blank=True, max_length=50000)
    footertext = models.TextField(u'Текст подвал (footer)', blank=True, max_length=50000)
    contacttext = models.TextField(u'Текст контакт (contact)', blank=True, max_length=50000)
    freetext = models.TextField(u'Текст (free)', blank=True, max_length=50000)
    
    def short_maintext(self):
        return short_text(self.maintext, 50)
    short_maintext.short_description = u'Текст'
    
    def short_maintext1(self):
        return short_text(self.maintext1, 50)
    short_maintext.short_description = u'Текст (1)'
    
    def short_footertext(self):
        return short_text(self.footertext, 50)
    short_maintext.short_description = u'Текст подвал (footer)'
    
    def short_contacttext(self):
        return short_text(self.contacttext, 50)
    short_maintext.short_description = u'Текст контакт (contact)'
    
    def short_freetext(self):
        return short_text(self.freetext, 50)
    short_maintext.short_description = u'Текст (free)'

