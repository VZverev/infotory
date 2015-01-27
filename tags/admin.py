from django.contrib import admin
from tags.models import Tag
# Register your models here.
class AdminTag(admin.ModelAdmin):
    list_display = ['title']
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
    
admin.site.register(Tag,AdminTag)