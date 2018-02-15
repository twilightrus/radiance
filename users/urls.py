from django.conf.urls import url

from . import views

app_name = "users"

urlpatterns = [
    url('register/', views.register, name='register'),
    url('auth/', views.auth, name='auth'),
    url('logout/', views.logout_user, name='logout'),
    ]
