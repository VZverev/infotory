from django.contrib import admin
from mainpage.models import ServiceModel, TextModel
from infotory.tinymce_settings import js_paths
# Register your models here.
class AdminService(admin.ModelAdmin):
    list_display = ['title']
    class Media:
        js = js_paths
        
class AdminText(admin.ModelAdmin):
    list_display = ['short_maintext', 'short_maintext1', 'short_footertext', 'short_contacttext', 'short_freetext']
    class Media:
        js = js_paths

admin.site.register(ServiceModel, AdminService)
admin.site.register(TextModel, AdminText)