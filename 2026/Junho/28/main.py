"""
simulador_gravidade_simples.py

Este script simula a queda de um objeto sob o efeito da gravidade em um terminal.
"""

import time

def simular_queda(altura_inicial, gravidade=9.8, intervalo=0.5):
    """
    Simula a queda de um objeto sob o efeito da gravidade.

    :param altura_inicial: Altura inicial do objeto em metros.
    :param gravidade: Aceleração da gravidade em m/s^2 (padrão é 9.8 m/s^2).
    :param intervalo: Intervalo de tempo entre as atualizações da simulação em segundos.
    """
    tempo = 0
    altura = altura_inicial

    while altura > 0:
        print(f"Tempo: {tempo:.1f}s - Altura: {altura:.2f}m")
        tempo += intervalo
        altura -= (gravidade * intervalo**2) / 2

        if altura < 0:
            altura = 0

        time.sleep(intervalo)

    print("O objeto atingiu o solo!")

def main():
    """
    Função principal que executa a simulação.
    """
    altura_inicial = 100  # Altura inicial em metros
    simular_queda(altura_inicial)

if __name__ == '__main__':
    main()