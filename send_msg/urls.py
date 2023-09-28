from django.urls import path
from . import views

#Caminho para as funções que enviam as mensagens
urlpatterns = [
    path('msg_1/', views.msg_1, name='msg_1'),
    path('msg_2/', views.msg_2, name='msg_2'),
    path('msg_3/', views.msg_3, name='msg_3')
]