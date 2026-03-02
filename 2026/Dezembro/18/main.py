"""
monitor_precos_passagens_aereas.py

Script para monitorar preços de voos para um destino específico e notificar sobre promoções.

Este script utiliza scraping para coletar informações sobre preços de voos de um site de voos.
Ele verifica se o preço está abaixo de um valor estabelecido e, se estiver, envia uma notificação.

Requisitos:
- Python 3.x
- Bibliotecas: requests, beautifulsoup4, smtplib

Uso:
python monitor_precos_passagens_aereas.py
"""

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações de notificação por email
SEU_EMAIL = 'seu_email@example.com'
SENHA_EMAIL = 'sua_senha'
DESTINATARIO_EMAIL = 'destinatario@example.com'

# Configurações de scraping
URL_VOO = 'https://www.exemplo.com/voos/para/destino'
PRECO_LIMITE = 500.0  # Preço em que você deseja ser notificado

def enviar_email(preco):
    """
    Envia um email com o preço do voo.

    :param preco: Preço do voo atual
    """
    msg = MIMEMultipart()
    msg['From'] = SEU_EMAIL
    msg['To'] = DESTINATARIO_EMAIL
    msg['Subject'] = 'Preço de Voo Promocional Encontrado!'

    body = f"O preço do voo para o seu destino caiu para R${preco:.2f}. Aproveite!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SEU_EMAIL, SENHA_EMAIL)
    text = msg.as_string()
    server.sendmail(SEU_EMAIL, DESTINATARIO_EMAIL, text)
    server.quit()

def obter_preco_voo():
    """
    Realiza o scraping para obter o preço do voo.

    :return: Preço do voo ou None se não encontrar
    """
    try:
        response = requests.get(URL_VOO)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Aqui você deve ajustar o seletor para encontrar o preço do voo no site específico
        preco_tag = soup.find('span', class_='preco-voo')
        if preco_tag:
            preco = float(preco_tag.text.replace('R$', '').replace(',', '.'))
            return preco
    except requests.RequestException as e:
        print(f"Erro ao obter o preço do voo: {e}")
    return None

def main():
    """
    Função principal que verifica o preço do voo e envia notificação se necessário.
    """
    preco = obter_preco_voo()
    if preco is not None and preco < PRECO_LIMITE:
        enviar_email(preco)
        print(f"Preço do voo abaixo do limite: R${preco:.2f}. Email enviado.")
    else:
        print("Preço do voo acima do limite ou erro ao obter preço.")

if __name__ == '__main__':
    main()