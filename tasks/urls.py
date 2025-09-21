from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('export_csv/', views.export_tasks_csv, name='export_tasks_csv'),
    path('signup/', views.signup, name='signup'),
]
