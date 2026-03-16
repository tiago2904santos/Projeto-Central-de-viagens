from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_hub, name='index'),
    path('hub/', views.hub, name='hub'),
]
