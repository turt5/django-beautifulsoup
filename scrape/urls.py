from django.urls import path
from scrape import views


urlpatterns = [
    path('apple/', views.apple, name='apple'),
    path('xiaomi/', views.xiaomi, name='xiaomi'),
    
]
