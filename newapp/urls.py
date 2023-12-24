from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewDetail, NewSearch, NewCreate, ArticleCreate, NewUpdate, ArticleUpdate, NewDelete, \
    ArticleDelete, CategoryListView, subscribe, unsubscribe, subscriptions, IndexView, error_error
from django.views.decorators.cache import cache_page



urlpatterns = [
    path('news/', NewsList.as_view(), name='new_list'),     # главная страница (1 минута)
    path('news/<int:pk>/', NewDetail.as_view(), name='new_detail'),
    path('news/search/', NewSearch.as_view(), name='new_search'),
    path('news/create/', NewCreate.as_view(success_url=''), name='new_create'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewUpdate.as_view(), name='new_update'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('news/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),

    path('index/', IndexView.as_view()),
    path('error/', error_error),

]


