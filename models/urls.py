from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth),
    path('users/', views.users, name='name_user'),
    path('list', views.list),
]
