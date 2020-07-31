"""todolist_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='todolist_home'),
    path('archive/', views.archive, name='todolist_archive'),
    path('deleteTask/<int:task_id>', views.deleteTask, name='delete_task'),
    path('archiveTask/<int:task_id>', views.archiveTask, name='archive_task'),
    path('unArchiveTask/<int:task_id>', views.unArchiveTask, name='un_archive_task'),
    path('updateTask/<int:task_id>', views.updateTask, name='updateTask'),
]
