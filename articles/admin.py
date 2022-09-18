from django.contrib import admin
from .models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'pk', 'title']
    search_fields = ['title', 'content']
    # search_help_text = "abra ka dabra"


admin.site.register(Article, ArticleAdmin)
