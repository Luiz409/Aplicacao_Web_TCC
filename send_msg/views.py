from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from django.http import HttpResponse
import urllib.parse

token = "123" #informação a ser escondida

def send_msg(msg, phoneList):  #função para enviar mensagem
    options = Options()
    options.add_argument("user-data-dir=your_path") 

    driver = webdriver.Chrome(options=options)
    
    #Para todos os números da lista, envia a mensagem.
    for phone in phoneList:
        link = f'https://web.whatsapp.com/send?phone={phone}&text={msg}'
        driver.get(link)

        #Espera até que o botão de enviar seja encontrado
        while driver.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span') == []:
            time.sleep(5)
        time.sleep(5)

        #Clica no botão de enviar
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(10)

    driver.close() #fecha o navegador

    return True

def msg_1(request): #função para enviar mensagem quando a primeira chave é desligada
    tokenReceived = request.GET.get("token", None)
    if tokenReceived == token:
        msg1 = "*Atenção*\n\nO nível da água está abaixando.\nPor favor, verifique o reservatório."
        msg1 = urllib.parse.quote(msg1)
        phoneList = ["whatapp_number"] #lista de números para enviar a mensagem
        send_msg(msg1, phoneList)
    return HttpResponse("ok")

def msg_2(request): #função para enviar mensagem quando a segunda chave é desligada
    tokenReceived = request.GET.get('token', None)
    if tokenReceived == token:
        msg2 = "*Atenção*\n\nO nível da água está no estado de alerta.\nPor favor, verifique o reservatório."
        msg2 = urllib.parse.quote(msg2)
        phoneList = ["whatapp_number"] #lista de números para enviar a mensagem
        send_msg(msg2, phoneList)
    return HttpResponse("ok")

def msg_3(request): #função para enviar mensagem quando a terceira chave é desligada
    tokenReceived = request.GET.get("token", None)
    if tokenReceived == token:
        msg3 = "*Atenção*\n\nO nível da água está no estado de emergência.\nPor favor, verifique o reservatório."
        msg3 = urllib.parse.quote(msg3)
        phoneList = ["whatapp_number"] #lista de números para enviar a mensagem
        send_msg(msg3, phoneList)
    return HttpResponse("ok")
