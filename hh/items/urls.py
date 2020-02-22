from django.urls import path
from . import views

app_name = 'items'
urlpatterns = [
    path('', views.index, name=''),
    path('list/', views.list, name='list'),
    path('count/', views.count, name='count'),
]
