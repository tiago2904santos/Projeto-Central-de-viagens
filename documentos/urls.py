from django.urls import path

from . import views

app_name = 'documentos'

urlpatterns = [
    path('', views.hub, name='hub'),
    path('oficios/', views.oficios_lista, name='oficios_lista'),
    path('oficios/novo/step1/', views.oficio_step1, name='oficio_step1'),
    path('oficios/novo/step2/', views.oficio_step2, name='oficio_step2'),
    path('oficios/novo/step3/', views.oficio_step3, name='oficio_step3'),
    path('oficios/novo/step4/', views.oficio_step4, name='oficio_step4'),
    path('oficios/novo/justificativa/', views.oficio_justificativa, name='oficio_justificativa'),
    path('oficios/novo/resumo/', views.oficio_resumo, name='oficio_resumo'),
    path('roteiros/', views.roteiros_lista, name='roteiros_lista'),
    path('justificativas/', views.justificativas_lista, name='justificativas_lista'),
    path('termos/', views.termos_lista, name='termos_lista'),
]
