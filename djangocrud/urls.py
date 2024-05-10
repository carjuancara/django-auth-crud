"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from tasks.views import signup, home, tasks, signout, signin, create_task, task_detail, complete_task, delete_task, tasks_completed
# aqui agregare rutas a mi projecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('tasks/', tasks, name='tasks'),
    path('tasks_completed/', tasks_completed , name='tasks_completed'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/<int:id>', task_detail, name='task_detail'),
    path('tasks/<int:id>/complete', complete_task, name='complete_task'),
    path('tasks/<int:id>/delete', delete_task , name='delete_task'),
    path('logout/', signout, name='logout'),
]
