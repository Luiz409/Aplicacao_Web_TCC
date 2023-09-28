from django.urls import path,include

#Caminho para as funções que enviam as mensagens
urlpatterns = [
    path('send_msg/',include('send_msg.urls')),
]
