from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastros_home, name='cadastros_home'),
]
