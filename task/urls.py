from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('<int:id>/completed/', views.TaskCompleted.as_view(), name='task_completed'),
    path('<int:id>', views.DeleteTask.as_view(), name='delete_task')

]