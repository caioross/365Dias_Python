"""
simulador_venda_ingressos.py

Este script implementa um sistema de reserva de assentos para cinema com um mapa visual em caracteres ASCII.
O usuário pode visualizar o mapa de assentos, selecionar assentos disponíveis e finalizar a reserva.
"""

import os

# Define o tamanho do cinema
LINHAS = 5
COLUNAS = 10

# Inicializa o mapa de assentos
assentos = [['L' for _ in range(COLUNAS)] for _ in range(LINHAS)]

def exibir_mapa():
    """
    Exibe o mapa de assentos atual.
    'L' representa um assento livre, 'O' representa um assento ocupado.
    """
    print("Mapa de Assentos:")
    for i, linha in enumerate(assentos):
        print(f"Linha {i+1}: {' '.join(linha)}")
    print("L - Livre, O - Ocupado")

def reservar_assento(linha, coluna):
    """
    Reserva um assento específico no mapa de assentos.

    :param linha: Índice da linha do assento (0-based)
    :param coluna: Índice da coluna do assento (0-based)
    :return: True se a reserva foi bem-sucedida, False se o assento já está ocupado
    """
    if assentos[linha][coluna] == 'L':
        assentos[linha][coluna] = 'O'
        return True
    return False

def main():
    """
    Função principal do script. Permite ao usuário visualizar o mapa de assentos,
    selecionar assentos disponíveis e finalizar a reserva.
    """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_mapa()
        try:
            linha = int(input("Digite o número da linha (1-5) ou 0 para sair: ")) - 1
            if linha == -1:
                print("Saindo do sistema.")
                break
            coluna = int(input("Digite o número da coluna (1-10): ")) - 1
            if 0 <= linha < LINHAS and 0 <= coluna < COLUNAS:
                if reservar_assento(linha, coluna):
                    print("Assento reservado com sucesso!")
                else:
                    print("Assento já ocupado. Por favor, escolha outro.")
            else:
                print("Linha ou coluna inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")

if __name__ == '__main__':
    main()