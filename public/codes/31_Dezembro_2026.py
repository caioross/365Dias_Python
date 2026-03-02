"""
resumo_365_scripts_python.py

Script para listar todos os títulos de scripts Python criados no ano e gerar um índice geral.
"""

import os
import datetime

def listar_scripts_ano(diretorio):
    """
    Lista todos os scripts Python criados no ano atual em um diretório específico.

    :param diretorio: Caminho do diretório onde os scripts estão armazenados.
    :return: Lista de títulos dos scripts criados no ano atual.
    """
    scripts_ano = []
    ano_atual = datetime.datetime.now().year

    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.py'):
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            # Obter a data de criação do arquivo
            data_criacao = datetime.datetime.fromtimestamp(os.path.getctime(caminho_arquivo))
            if data_criacao.year == ano_atual:
                scripts_ano.append(nome_arquivo)

    return scripts_ano

def gerar_indice(scripts):
    """
    Gera um índice geral a partir de uma lista de títulos de scripts.

    :param scripts: Lista de títulos dos scripts.
    :return: String contendo o índice geral.
    """
    indice = "Índice de Scripts Python Criados no Ano:\n"
    for i, script in enumerate(scripts, start=1):
        indice += f"{i}. {script}\n"
    return indice

def main():
    """
    Função principal que executa o script.
    """
    diretorio_scripts = 'caminho/para/seus/scripts'  # Substitua pelo caminho correto
    scripts_ano = listar_scripts_ano(diretorio_scripts)
    indice_geral = gerar_indice(scripts_ano)
    print(indice_geral)

if __name__ == '__main__':
    main()