from . import views
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls import handler500

handler500 = 'todo.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signup),
    path('loginn/', views.loginn),
    path('todopage', views.todopage),
    path('delete_todo/<int:srno>', views.delete_todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('signout/', views.signout, name='signout'),
    
]
