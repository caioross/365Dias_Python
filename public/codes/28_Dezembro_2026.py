"""
simulador_fogo_artificio_terminal.py

Este script simula a explosão de fogos de artifício em um terminal usando ASCII art.
"""

import random
import time
import os

# Cores ANSI para o terminal
COLORES = [
    "\033[91m",  # Vermelho
    "\033[92m",  # Verde
    "\033[93m",  # Amarelo
    "\033[94m",  # Azul
    "\033[95m",  # Magenta
    "\033[96m",  # Ciano
    "\033[97m",  # Branco
]

# Limpa o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gera uma explosão de fogo de artifício
def gerar_explosao(x, y, tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            if (i - tamanho // 2) ** 2 + (j - tamanho // 2) ** 2 <= (tamanho // 2) ** 2:
                print(random.choice(COLORES) + '*', end='')
            else:
                print(' ', end='')
        print()
    print("\033[0m", end='')  # Reseta a cor

# Simula a explosão de fogos de artifício
def simular_explosao():
    limpar_terminal()
    largura = 80
    altura = 24
    for _ in range(10):  # Simula 10 fogos de artifício
        x = random.randint(0, largura - 1)
        y = random.randint(0, altura - 1)
        tamanho = random.randint(3, 7)
        gerar_explosao(x, y, tamanho)
        time.sleep(0.5)
        limpar_terminal()

def main():
    simular_explosao()

if __name__ == '__main__':
    main()