from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
    path('logout/',views.user_logout,name='logout'),

    
]