"""
gerador_lista_presenca_qr.py

Este script gera um QR Code que aponta para um formulário de presença e gera a lista em CSV.
"""

import qrcode
import csv
from datetime import datetime

def gerar_qr_code(url_formulario, nome_arquivo):
    """
    Gera um QR Code com a URL do formulário de presença.

    :param url_formulario: URL do formulário de presença.
    :param nome_arquivo: Nome do arquivo onde o QR Code será salvo.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url_formulario)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)
    print(f"QR Code salvo como {nome_arquivo}")

def gerar_csv(nomes_participantes, nome_arquivo):
    """
    Gera um arquivo CSV com os nomes dos participantes.

    :param nomes_participantes: Lista de nomes dos participantes.
    :param nome_arquivo: Nome do arquivo CSV a ser gerado.
    """
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Data'])
        for nome in nomes_participantes:
            writer.writerow([nome, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    print(f"CSV salvo como {nome_arquivo}")

def main():
    url_formulario = "https://forms.gle/ExemploDeFormulario"
    nome_arquivo_qr = "qr_code_presenca.png"
    nome_arquivo_csv = "lista_presenca.csv"
    nomes_participantes = ["João", "Maria", "Carlos", "Ana"]

    gerar_qr_code(url_formulario, nome_arquivo_qr)
    gerar_csv(nomes_participantes, nome_arquivo_csv)

if __name__ == '__main__':
    main()