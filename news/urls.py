from django.urls import path
from .views import news_view, create_view, NewsDetailView, NewsUpdateView, NewsDeleteView

app_name = 'news'

urlpatterns = [
    path('', news_view, name='news_view'),
    path('create', create_view, name='create_view'),
    path('<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news-delete'),
]
