# -*- coding: utf-8 -*- 
from django.db import models
from tags.models import Tag

def upload_image(instance, filename):     
    return '.calendar/images/%s_%s%s' % (filename[:filename.rfind('.')] , get_random_string(length=4), filename[filename.rfind('.'):]) 

def upload_file(instance, filename):     
        return '.calendar/files/%s_%s%s' % (filename[:filename.rfind('.')] , get_random_string(length=4), filename[filename.rfind('.'):]) 

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

