from django.contrib import admin
from resources.models import Image, File
# Register your models here.
class AdminFile(admin.ModelAdmin):
    list_display = ['title', 'admin_file_info']
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
        
class AdminImage(admin.ModelAdmin):
    list_display = ['title', 'show_image', 'show_tags']
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )

admin.site.register(Image,AdminImage)
admin.site.register(File,AdminFile)