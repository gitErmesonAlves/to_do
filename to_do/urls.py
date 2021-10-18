from django.contrib import admin
from django.urls import path
from models import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.auth),
    path('users/<str:name_user>', views.users, name='name_user'),
    path('list', views.list),
]
