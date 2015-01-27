from django.contrib import admin
from tags.models import Tag
from infotory.tinymce_settings import js_paths
# Register your models here.
class AdminTag(admin.ModelAdmin):
    list_display = ['title']
    class Media:
        js = js_paths
    
admin.site.register(Tag,AdminTag)