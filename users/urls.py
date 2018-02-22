from django.conf.urls import url

from django.urls import path

from . import views

from .views import RegisterView

app_name = "users"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout_user, name='logout'),
    ]
