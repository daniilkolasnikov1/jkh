from django.urls import path
from . import views

urlpatterns = [
    path('', views.vidyrabot_home, name='vidyrabot_home'),
    path('create', views.create, name='create'),
]
