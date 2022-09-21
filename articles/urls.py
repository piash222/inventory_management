from django.urls import path
from .views import article_list, article_detail, article_search_view

urlpatterns = [
    path('', article_list),
    path('article/', article_search_view),
    path('article/<int:pk>', article_detail)
]
