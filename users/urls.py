from django.urls import path

from . import views
from .views import *


app_name = "users"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('auth/', AuthView.as_view(), name='auth'),
    path('logout/', views.logout_user, name='logout'),
    ]
