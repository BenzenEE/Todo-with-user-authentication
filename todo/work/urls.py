from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('add_task', views.add_task, name='addTask'),
    path('delete-task/<int:id>', views.delete_task, name='deleteTask'),
    path('change-status/<int:id>/<str:status>',views.change_status,name='changeStatus'),
    path('logout/', views.logout, name='logout'),
    path('edit-task/<int:id>', views.edit_task, name='editTask'),
    path('update-task/<int:id>', views.update_task, name='updateTask'),
]