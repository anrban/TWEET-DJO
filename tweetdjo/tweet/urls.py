from . import views
from django.urls import path

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('edit/<int:tweet_id>', views.tweet_edit, name='tweet_edit'),
    path('delete/<int:tweet_id>', views.tweet_delete, name='tweet_delete'),
    path('delete/<int:tweet_id>', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login_view'),
    path('logout/', views.logout, name='logout_view'),
]