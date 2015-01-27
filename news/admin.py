from django.contrib import admin
from news.models import Article, Comment
# Register your models here.
from infotory.tinymce_settings import js_paths

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    
class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'show_author', 'pub_date', 'show_tags', 'get_raiting']
    inlines = [CommentInline]
    class Media:
        js = js_paths
        
class AdminComment(admin.ModelAdmin):
    list_display = ['title', 'show_author', 'pub_date', 'show_short_text']
    class Media:
        js = js_paths
        
admin.site.register(Article,AdminArticle)
admin.site.register(Comment,AdminComment)