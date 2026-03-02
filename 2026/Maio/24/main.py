"""
gerador_codigo_barras.py

Gera uma imagem de código de barras padrão EAN-13 a partir de uma sequência numérica.
"""

import barcode
from barcode.writer import ImageWriter

def gerar_codigo_barras(ean_number):
    """
    Gera uma imagem de código de barras EAN-13.

    Args:
        ean_number (str): O número EAN-13 como uma string de 12 ou 13 dígitos.

    Returns:
        None: Salva a imagem do código de barras em um arquivo.
    """
    # Verifica se o número EAN-13 é válido
    if len(ean_number) == 12:
        ean_number = '0' + ean_number
    elif len(ean_number) != 13:
        raise ValueError("O número EAN-13 deve ter 12 ou 13 dígitos.")

    # Cria o código de barras
    ean = barcode.get_barcode_class('ean13')
    ean_barcode = ean(ean_number, writer=ImageWriter())

    # Salva a imagem do código de barras
    ean_barcode.save('codigo_barras')

def main():
    """
    Função principal que executa o script.
    """
    ean_number = input("Digite o número EAN-13 (12 ou 13 dígitos): ")
    try:
        gerar_codigo_barras(ean_number)
        print("Código de barras gerado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()