import time

def exemplo_algoritmo():
    """
    Função de exemplo que simula um algoritmo com um tempo de execução aleatório.
    """
    soma = 0
    for i in range(1, 1000000):
        soma += i
    return soma

def estimar_tempo_execucao(funcao):
    """
    Função para estimar o tempo de execução de um algoritmo.
    
    :param funcao: Função cujo tempo de execução será estimado.
    :return: Tempo de execução da função em segundos.
    """
    # Registra o tempo de início
    inicio = time.time()

    # Executa a função fornecida
    funcao()

    # Registra o tempo de término
    fim = time.time()

    # Calcula e retorna a diferença de tempo
    tempo_execucao = fim - inicio
    return tempo_execucao

def main():
    """
    Função principal que executa a estimativa de tempo de execução de um algoritmo.
    """
    print("Estimando o tempo de execução do algoritmo...\n")

    # Estimar o tempo de execução do exemplo de algoritmo
    tempo = estimar_tempo_execucao(exemplo_algoritmo)
    
    print(f"Tempo de execução do algoritmo: {tempo:.6f} segundos")

if __name__ == "__main__":
    main()
