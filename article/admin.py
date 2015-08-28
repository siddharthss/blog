from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_date', 'user_fk')

admin.site.register(Article, ArticleAdmin)

