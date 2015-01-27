from django.contrib import admin
from infotory.tinymce_settings import js_paths
from events.models import Event
from tags.models import Tag
from news.models import Article

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Article
    extra = 1
    
class AdminEvent(admin.ModelAdmin):
    list_display = ['title', 'desc_short', 'start_date', 'end_date']
    inlines = [ArticleInline]
    class Media:
        js = js_paths
    
admin.site.register(Event,AdminEvent)