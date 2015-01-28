# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime 
from news.models import Article, Comment
from news.forms import CommentForm
# Create your views here.
def index(request):
    entries = Article.objects.all()
    return render_to_response('news.html', { 'title': "Новости", 'entries': entries})
 
def details(request, id):
    comment_form = CommentForm()
    entry = get_object_or_404(Article, pk=id)        
    return render_to_response('article.html', 
                              { 'title': "Новости", 'entry': entry, 'form': comment_form }, 
                              context_instance=RequestContext(request)
                              )

def add_comment(request, id):  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid(): 
            entry = Article.objects.get(pk=id)
            comment = Comment(title = form.cleaned_data['title'], text = form.cleaned_data['text'])
            entry.comments.add(comment)
            comment_data = {
                                 'author': comment.author,
                                 'title': comment.title,
                                 'text': comment.text,
                                 'pub_date': comment.pub_date,
                                 }
            data = JsonResponse(comment_data)
            return HttpResponse(data)
        else:
            return HttpResponse(False)
    else:
        return HttpResponseRedirect('/news/'+id+'/')


    
    
    