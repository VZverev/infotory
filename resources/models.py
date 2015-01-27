# -*- coding: utf-8 -*- 
import os
from infotory.settings import MEDIA_ROOT
from django.utils.crypto import get_random_string
from django.db import models
from tags.models import Tag

def upload_image(instance, filename):     
    return 'resources/images/%s_%s%s' % (filename[:filename.rfind('.')] , get_random_string(length=4), filename[filename.rfind('.'):]) 

def upload_file(instance, filename):     
        return 'resources/files/%s_%s%s' % (filename[:filename.rfind('.')] , get_random_string(length=4), filename[filename.rfind('.'):]) 

class Image(models.Model):
    title = models.CharField(u'Название', max_length=40, blank=True)
    desc_short = models.TextField(u'Краткое описание',blank=True)
    file = models.ImageField(u'Файл', upload_to=upload_image)
    tag = models.ManyToManyField(Tag, verbose_name='Тэг', blank=True, null=True)
    
    class Meta():
        db_table = 'resources_image'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering=['title']
        
    def __unicode__(self):
        return self.title
    
    def show_image(self):
        if self.file:
            return '<img src="' + self.file.url  + '" style="width: 50px; height: 50px;">'
        else:
            return ''
    show_image.short_description = u'Миниатюра'
    show_image.allow_tags = True
    
    def show_tags(self):
        if self.tag:
            return "\n".join([t.title for t in self.tag.all()])
        else:
            return ""
    show_tags.short_description = u'Тэги'
    
class File(models.Model):
    title = models.CharField(u'Название', max_length=40)
    file = models.FileField(u'Файл', upload_to=upload_file)
    desc_short = models.TextField(u'Краткое описание',blank=True)
    tag = models.ManyToManyField(Tag, verbose_name='Тэг', blank=True, null=True)
    
    class Meta():
        db_table = 'resources_file'
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering=['title']
        
    def __unicode__(self):
        return self.title
    
    def admin_file_info(self):
        if self.file:
            file_path = self.file.url
            return file_path
        else:
            return "File not exist"
            
        
    admin_file_info.short_description = u'Информация'
    admin_file_info.allow_tags = True
