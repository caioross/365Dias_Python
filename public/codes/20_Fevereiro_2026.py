"""
Script para listar os nomes de todos os processos ativos no computador.

Este script utiliza a biblioteca psutil para obter informações sobre os processos
ativos no sistema operacional. Ele imprime o nome de cada processo em execução.

Requisitos:
- psutil (instalável via pip: pip install psutil)
"""

import psutil

def listar_processos_ativos():
    """
    Lista os nomes de todos os processos ativos no computador.

    Returns:
        list: Uma lista contendo os nomes dos processos ativos.
    """
    processos = []
    for processo in psutil.process_iter(['name']):
        try:
            processos.append(processo.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processos

def main():
    """
    Função principal que lista e imprime os processos ativos.
    """
    processos_ativos = listar_processos_ativos()
    print("Processos ativos no computador:")
    for processo in processos_ativos:
        print(processo)

if __name__ == '__main__':
    main()