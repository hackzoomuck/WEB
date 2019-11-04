from django.urls import path
from  . import views

app_name = 'movies'

urlpatterns = [
    path('',views.index, name='index'),
    path('new/',views.new, name='new'), #new에 db에 data 넣는 것 :restful(create))
    path('<int:pk>/',views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]

