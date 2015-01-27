from django.contrib import admin
from resources.models import Image, File
from infotory.tinymce_settings import js_paths
# Register your models here.
class AdminFile(admin.ModelAdmin):
    list_display = ['title', 'admin_file_info']
    class Media:
        js = js_paths
        
class AdminImage(admin.ModelAdmin):
    list_display = ['title', 'show_image', 'show_tags']
    class Media:
        js = js_paths

admin.site.register(Image,AdminImage)
admin.site.register(File,AdminFile)