from django.contrib import admin

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
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
    
admin.site.register(Event,AdminEvent)