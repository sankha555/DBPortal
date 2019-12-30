from django.contrib import admin
from django.urls import path
from .views import register, update_staff, change_email, change_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('update_staff/', update_staff, name='update_staff'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('change_email/', change_email, name='change_email'),
    path('change_password/', change_password, name='change_password'),
]
