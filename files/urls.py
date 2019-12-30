from django.contrib import admin
from django.urls import path
from .views import upload_file, search_dber, search_uid_normal, update_dber, search_city_staff, delete_dber, add_dber, send_mail, send_mass_mails, home, link_account
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', home, name='home'),
    path('upload_file/', upload_file, name='upload_file'),
    path('search_dber/', search_dber, name='search_dber'),
    path('search_uid/', search_uid_normal, name='search_uid_normal'),
    path('search_city_staff/', search_city_staff, name='search_city_staff'),
    path('link_account/<int:pk>/', link_account, name='link_account'),
    path('update_dber/<int:pk>/', update_dber, name='update_dber'),
    path('delete_dber/<int:pk>/', delete_dber, name='delete_dber'),
    path('add_dber/', add_dber, name='add_dber'),
    path('send_mail/<int:pk>/', send_mail, name='send_mail'),
    path('send_mass_mails/', send_mass_mails, name='send_mass_mails'),
]
