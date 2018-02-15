from django.conf.urls import url

from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout_user, name='logout'),
    ]
