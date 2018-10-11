from django.urls import path
from . import views

app_name = 'CatApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.ListView.as_view(), name='list'),
    path('new_cat/', views.new_cat, name='new_cat'),
    path('delete_cat/<int:cat_id>', views.delete_cat, name='delete_cat')
]
