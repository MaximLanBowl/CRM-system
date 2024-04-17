from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import (
    TaskListView,
    TaskUpdateView,
    calendar_view,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,

)

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('new/', TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('calendar/', calendar_view, name='calendar'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>', TaskDetailView.as_view(), name='details'),
    path('tasks_report/', views.tasks_report, name='tasks_report'),
]