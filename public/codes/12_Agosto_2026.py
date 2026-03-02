"""
Script para gerar um QR Code que adiciona um contato à agenda do celular.
Utiliza a biblioteca qrcode para criar o QR Code e a biblioteca vobject para criar o vCard.
"""

import qrcode
from vobject import vCard

def criar_vcard(nome, telefone, email, endereco):
    """
    Cria um vCard com as informações fornecidas.

    :param nome: Nome do contato
    :param telefone: Número de telefone do contato
    :param email: Email do contato
    :param endereco: Endereço do contato
    :return: String do vCard
    """
    vcard = vCard()
    vcard.add('fn').value = nome
    vcard.add('tel').value = telefone
    vcard.add('email').value = email
    vcard.add('adr').value = endereco
    return vcard.serialize()

def gerar_qr_code(dados, nome_arquivo):
    """
    Gera um QR Code com os dados fornecidos e salva em um arquivo.

    :param dados: Dados a serem codificados no QR Code
    :param nome_arquivo: Nome do arquivo onde o QR Code será salvo
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)

def main():
    """
    Função principal que cria um vCard e gera um QR Code correspondente.
    """
    nome = "João Silva"
    telefone = "+55 11 99999-9999"
    email = "joao.silva@example.com"
    endereco = "Rua dos Bobos, 000, São Paulo, SP"

    vcard_str = criar_vcard(nome, telefone, email, endereco)
    gerar_qr_code(vcard_str, "contato_qr_code.png")

if __name__ == '__main__':
    main()