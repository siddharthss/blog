from django.shortcuts import render, redirect
from .models import Article
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):
    article_list = Article.objects.all()
    return render(request, 'article/index.html', {'article_list': article_list})

@login_required
def display_view(request, article_id):
    search_article = Article.objects.get(pk=article_id)
    return render(request, 'article/display.html', {'search_article': search_article,'user_req':request.user})

@login_required
def create_view(request):
    return render(request, 'article/create.html',)

@login_required
def add_view(request):
    title = request.POST['title']
    user = request.user
    user_object = User.objects.get(first_name=user.first_name)
    pub_date = request.POST['pub_date']
    content = request.POST['content']
    art = Article.objects.create(title=title, user_fk=user_object , pub_date=pub_date, update_date=pub_date, content=content)
    art.save()
    return redirect(index_view)

@login_required
def delete_view(request, article_id):
    delete_article = Article.objects.get(pk=article_id)
    delete_article.delete()
    return redirect(index_view)

@login_required
def update_content_view(request, article_id):
    search_article = Article.objects.get(pk=article_id)
    search_article.content = request.POST['update_content']
    search_article.title = request.POST['update_title']
    search_article.update_date = timezone.now()
    search_article.save()
    return redirect(display_view,search_article.id)
