import random
import time

def sorteio_mega_sena():
    """
    Realiza um sorteio da Mega-Sena, retornando uma lista com 6 números únicos entre 1 e 60.
    """
    return sorted(random.sample(range(1, 61), 6))

def simular_sorteios(target_draw):
    """
    Simula sorteios da Mega-Sena até que o sorteio alvo seja atingido.
    
    :param target_draw: A sequência de números que estamos tentando ganhar.
    :return: O número de sorteios necessários para ganhar.
    """
    sorteios = 0
    while True:
        sorteios += 1
        if sorteio_mega_sena() == target_draw:
            return sorteios

def main():
    """
    Função principal que executa a simulação de sorteios e mede o tempo necessário para ganhar na Mega-Sena.
    """
    target_draw = sorteio_mega_sena()  # Sorteio alvo
    print(f"Sorteio alvo: {target_draw}")
    
    start_time = time.time()
    sorteios_necessarios = simular_sorteios(target_draw)
    end_time = time.time()
    
    tempo_decorrido = end_time - start_time
    print(f"Número de sorteios necessários para ganhar: {sorteios_necessarios}")
    print(f"Tempo decorrido: {tempo_decorrido:.2f} segundos")

if __name__ == '__main__':
    main()