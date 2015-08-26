from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def index_view(request):
    """ view to display all object on index page and render article/index.html"""
    user = request.user
    article_list = Article.objects.all()
    return render(request, 'article/index.html', {'article_list': article_list, 'user_req': user})


@login_required
def display_view(request, article_id):
    """ view to display selected object on display page and render article/display.html"""
    search_article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article/display.html', {'search_article': search_article,'user_req':request.user})

@login_required
def create_view(request):
    """ view to render article/create.html"""
    return render(request, 'article/create.html',)

@login_required
def add_view(request):
    """ view to accept form data from the create form and
    add the new article details in Article model and redirect to index_view """
    title = request.POST['title']
    user = request.user
    user_object = User.objects.get(first_name=user.first_name)
    pub_date = request.POST['pub_date']
    content = request.POST['content']
    art = Article.objects.create(title=title, user_fk=user_object , pub_date=pub_date, update_date=pub_date, content=content)
    messages.success(request,'New Article created')
    return redirect(index_view)

@login_required
def delete_view(request, article_id):
    """ view to delete object on index page and redirect to index_view """
    delete_article = Article.objects.get(pk=article_id)
    delete_article.delete()
    messages.success(request,'Article deleted')
    return redirect(index_view)

@login_required
def update_content_view(request, article_id):
    """ view to accept form data from the display form and
    update the selected  article details in Article model and
    redirect to display_View with argument search_article.id """
    search_article = Article.objects.get(pk=article_id)
    search_article.content = request.POST['update_content']
    search_article.title = request.POST['update_title']
    search_article.update_date = timezone.now()
    search_article.save()
    messages.success(request,'Article  updated')
    return redirect(display_view,search_article.id)
