# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, get_object_or_404

from news.models import Article, Comment
# Create your views here.
def index(request):
    entries = Article.objects.all()
    return render_to_response('news.html', { 'title': "Новости", 'entries': entries})
 
def details(request, id):
    entry = get_object_or_404(Article, pk=id)
        
    return render_to_response('article.html', { 'title': "Новости", 'entry': entry})