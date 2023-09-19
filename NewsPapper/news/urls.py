from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('search/', views.news_search, name='news_search'),
    path('add/', views.NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/', views.NewsEditView.as_view(), name='news_edit'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),
]
