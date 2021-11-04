from django.contrib import admin
from django.urls import path
from .views import index,get_tasks,get_task,update_task, delete_task

urlpatterns = [
    path('home/', index),
    path('task/', get_tasks, name='get_tasks'),
    path('view/<int:task_id>', get_task, name='get_task'),
    path('update/<int:task_id>', update_task, name='update_task'),
    path('delete/<int:task_id>', delete_task, name='delete_task')

]