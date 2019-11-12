from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
   path('', views.index, name='index'), #/articles/ 
   path('new/', views.new, name='new'),
   path('<int:pk>/', views.detail, name='detail'), #/articles/1/
   path('<int:pk>/', views.edit, name='edit'), #/articles
]
