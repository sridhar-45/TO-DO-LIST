from django.urls import path 
from .views import task_list, task_create, task_update, task_delete, task_complete

urlpatterns = [
    path('', task_list , name = "task_list"),
    path('add/', task_create, name = "task_create"),     #url for adding a new task
    path('edit/<int:pk>/', task_update, name = "task_update"),
    path('delete/<int:pk>/', task_delete, name = "task_delete"),
    path('complete/<int:pk>/', task_complete, name = "task_complete")
    
]
