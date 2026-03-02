import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

def load_gift_suggestions(filename):
    """
    Carrega sugestões de presentes de um arquivo de texto.

    Args:
        filename (str): O nome do arquivo que contém as sugestões de presentes.

    Returns:
        list: Uma lista de sugestões de presentes.
    """
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def assign_gifts(participants, gift_suggestions):
    """
    Atribui sugestões de presentes a participantes de forma aleatória.

    Args:
        participants (list): Uma lista de nomes de participantes.
        gift_suggestions (list): Uma lista de sugestões de presentes.

    Returns:
        dict: Um dicionário com participantes como chaves e sugestões de presentes como valores.
    """
    random.shuffle(gift_suggestions)
    return dict(zip(participants, gift_suggestions))

def send_email(participant, gift, sender_email, sender_password, recipient_email):
    """
    Envia um e-mail com a sugestão de presente para o participante.

    Args:
        participant (str): O nome do participante.
        gift (str): A sugestão de presente.
        sender_email (str): O endereço de e-mail do remetente.
        sender_password (str): A senha do e-mail do remetente.
        recipient_email (str): O endereço de e-mail do destinatário.
    """
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Sua sugestão de presente para o amigo secreto!'

    body = f'Olá, {participant}!\n\nSua sugestão de presente para o amigo secreto é: {gift}\n\nBoa sorte!'
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f'E-mail enviado com sucesso para {participant}.')
    except Exception as e:
        print(f'Erro ao enviar e-mail para {participant}: {e}')

def main():
    participants = ['Alice', 'Bob', 'Charlie', 'David']
    gift_suggestions = load_gift_suggestions('gifts.txt')
    gift_assignments = assign_gifts(participants, gift_suggestions)

    sender_email = 'seu_email@gmail.com'
    sender_password = 'sua_senha'

    for participant, gift in gift_assignments.items():
        send_email(participant, gift, sender_email, sender_password, participant.lower() + '@example.com')

if __name__ == '__main__':
    main()