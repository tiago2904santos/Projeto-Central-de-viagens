from django.urls import path

from . import views

app_name = 'cadastros'

urlpatterns = [
    path('', views.cadastros_home, name='cadastros_home'),
]
