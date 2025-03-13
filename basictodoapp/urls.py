from django.urls import path

from basictodoapp import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('task/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]