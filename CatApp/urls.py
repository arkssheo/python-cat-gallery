from django.urls import path
from . import views

app_name = 'CatApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.ListView.as_view(), name='list')
]
