from django.urls import path 
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('article<int:pk>', views.ArticleDetailView.as_view(), name='article_page'),
    path('articles/new', views.ArticleCreateView.as_view(), name='new_articles'),
    path('articles<int:pk>/edit', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('articles<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),
]