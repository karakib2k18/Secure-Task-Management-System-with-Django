from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Root URL points to task_list
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/tasks/', views.category_tasks, name='category_tasks'),
]
