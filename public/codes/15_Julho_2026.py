import psutil

def get_top_cpu_processes(n=5):
    """
    Retorna uma lista dos n processos com maior consumo de CPU.

    :param n: Número de processos a serem retornados.
    :return: Lista de tuplas contendo o nome do processo e o percentual de CPU utilizado.
    """
    # Obtém a lista de todos os processos
    processes = psutil.process_iter(['pid', 'name', 'cpu_percent'])
    
    # Ordena os processos pelo percentual de CPU utilizado
    sorted_processes = sorted(processes, key=lambda p: p.info['cpu_percent'], reverse=True)
    
    # Retorna os n primeiros processos da lista ordenada
    return [(p.info['name'], p.info['cpu_percent']) for p in sorted_processes[:n]]

def main():
    """
    Função principal do script. Lista os 5 processos com maior consumo de CPU.
    """
    top_processes = get_top_cpu_processes()
    print("Top 5 processos com maior consumo de CPU:")
    for name, cpu_percent in top_processes:
        print(f"Nome: {name}, CPU: {cpu_percent}%")

if __name__ == '__main__':
    main()