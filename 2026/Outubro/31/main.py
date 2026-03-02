"""
simulador_fantasma_halloween.py

Este script gera sons assustadores e frases de terror aleatórias em uma interface temática de Halloween.
"""

import random
import time
import os

# Lista de sons assustadores (simulação)
sons_assustadores = [
    "ruído de passos",
    "grito de medo",
    "vento soprando",
    "som de porta se abrindo"
]

# Lista de frases de terror
frases_terror = [
    "Você não deveria estar aqui...",
    "A noite é minha...",
    "Prepare-se para o terror...",
    "Não tente correr..."
]

def reproduzir_som(som):
    """
    Simula a reprodução de um som assustador.
    
    :param som: Nome do som a ser reproduzido.
    """
    print(f"\nTocando: {som.upper()}")
    time.sleep(2)  # Simula o tempo de reprodução do som

def exibir_frase(frase):
    """
    Exibe uma frase de terror na tela.
    
    :param frase: Frase de terror a ser exibida.
    """
    print(f"\n{frase}")
    time.sleep(3)  # Tempo para a frase ser lida

def main():
    """
    Função principal que controla a simulação do fantasma de Halloween.
    """
    print("Bem-vindo ao Simulador de Fantasma de Halloween!")
    input("Pressione Enter para começar...")

    while True:
        # Escolhe um som e uma frase aleatórios
        som = random.choice(sons_assustadores)
        frase = random.choice(frases_terror)

        # Reproduz o som e exibe a frase
        reproduzir_som(som)
        exibir_frase(frase)

        # Pergunta ao usuário se deseja continuar
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("Obrigado por jogar! Tenha um Halloween assustador!")

if __name__ == '__main__':
    main()