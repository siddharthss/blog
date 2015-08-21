from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    article_list = Article.objects.all()
    return render(request, 'article/index.html', {'article_list': article_list})

@login_required
def displayview(request, article_id):
    search_article = Article.objects.get(pk=article_id)
    return render(request, 'article/display.html', {'search_article': search_article})

@login_required
def createview(request):
    return render(request, 'article/create.html',)

@login_required
def addview(request):
    title=request.POST['title']
    user=request.user
    user_object=User.objects.get(first_name=user.first_name)
    pub_date=request.POST['pub_date']
    content=request.POST['content']
    art=Article.objects.create(title=title, user_fk=user_object , pub_date=pub_date, content=content)
    art.save()
    return redirect(index)

@login_required
def deleteview(request, article_id):
    delete_article = Article.objects.get(pk=article_id)
    delete_article.delete()
    return redirect(index)
