from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.recebeligacao, name='recebeligacao'),
    path('lista_chamadas/', views.lista_chamadas, name='lista_chamadas'),
    path('novas_chamadas/', views.novas_chamadas, name='novas_chamadas'),
    path('recebeligacao/', views.recebeligacao, name='recebeligacao')
]
