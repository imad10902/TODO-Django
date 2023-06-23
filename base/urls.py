from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.addTask, name='add-task'),
    path('update-task/<str:pk>', views.updateTask, name='update-task'),
    path('delete-task/<str:pk>', views.deleteTask, name='delete-task'),
    path('delete-task/', views.deleteAll, name='delete-all'),
    path('login-page/', views.loginPage, name='login-page'),
    path('register-page/', views.registerPage, name='register-page'),
    path('logout-user/', views.logoutUser, name='logout-user'),
]