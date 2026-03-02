"""
simulador_processamento_paralelo.py

Este script demonstra a diferença de tempo entre execução sequencial e usando Multi-processing.
"""

import time
from multiprocessing import Pool

def tarefa_demorada(x):
    """
    Simula uma tarefa demorada.
    
    Args:
    x (int): Um número para simular a duração da tarefa.
    
    Returns:
    int: O número recebido.
    """
    time.sleep(1)  # Simula uma tarefa que leva 1 segundo para ser concluída
    return x

def execucao_sequencial(tarefas):
    """
    Executa as tarefas de forma sequencial.
    
    Args:
    tarefas (list): Uma lista de tarefas a serem executadas.
    
    Returns:
    list: Os resultados das tarefas.
    """
    resultados = []
    for tarefa in tarefas:
        resultado = tarefa_demorada(tarefa)
        resultados.append(resultado)
    return resultados

def execucao_paralela(tarefas):
    """
    Executa as tarefas de forma paralela usando Multi-processing.
    
    Args:
    tarefas (list): Uma lista de tarefas a serem executadas.
    
    Returns:
    list: Os resultados das tarefas.
    """
    with Pool(processes=4) as pool:
        resultados = pool.map(tarefa_demorada, tarefas)
    return resultados

def main():
    """
    Função principal que executa o simulador de processamento paralelo.
    """
    tarefas = list(range(10))  # Simula 10 tarefas
    
    print("Execução Sequencial:")
    inicio_sequencial = time.time()
    resultados_sequencial = execucao_sequencial(tarefas)
    fim_sequencial = time.time()
    print(f"Tempo de execução sequencial: {fim_sequencial - inicio_sequencial:.2f} segundos")
    print(f"Resultados: {resultados_sequencial}")
    
    print("\nExecução Paralela:")
    inicio_paralelo = time.time()
    resultados_paralelo = execucao_paralela(tarefas)
    fim_paralelo = time.time()
    print(f"Tempo de execução paralela: {fim_paralelo - inicio_paralelo:.2f} segundos")
    print(f"Resultados: {resultados_paralelo}")

if __name__ == '__main__':
    main()