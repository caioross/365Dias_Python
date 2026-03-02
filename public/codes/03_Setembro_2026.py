"""
Extrator de Comentários de Código
=================================

Este script percorre arquivos .py em um diretório especificado e extrai todas as docstrings presentes.
As docstrings são coletadas e armazenadas em um arquivo de saída para documentação externa.

Uso
---
Execute o script no diretório onde os arquivos .py estão localizados. O arquivo de saída será criado no mesmo diretório.

Autor: [Seu Nome]
Data: [Data Atual]
"""

import os
import re

def extrair_docstrings(diretorio):
    """
    Extrai docstrings de todos os arquivos .py no diretório especificado.

    :param diretorio: Caminho para o diretório contendo os arquivos .py.
    :return: Um dicionário com nomes de arquivos como chaves e suas docstrings como valores.
    """
    docstrings = {}
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.py'):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                conteudo = file.read()
                # Regex para encontrar docstrings no início de funções ou classes
                matches = re.findall(r'"""(.*?)"""', conteudo, re.DOTALL)
                if matches:
                    docstrings[arquivo] = matches[0].strip()
    return docstrings

def salvar_docstrings(docstrings, arquivo_saida):
    """
    Salva as docstrings extraídas em um arquivo de texto.

    :param docstrings: Dicionário com nomes de arquivos como chaves e suas docstrings como valores.
    :param arquivo_saida: Nome do arquivo onde as docstrings serão salvas.
    """
    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        for arquivo, docstring in docstrings.items():
            file.write(f"Arquivo: {arquivo}\n")
            file.write(f"Docstring: {docstring}\n\n")

def main():
    """
    Função principal que coordena a extração e salvamento das docstrings.
    """
    diretorio = os.getcwd()  # Diretório atual
    arquivo_saida = 'documentacao.txt'
    docstrings = extrair_docstrings(diretorio)
    salvar_docstrings(docstrings, arquivo_saida)
    print(f"Docstrings extraídas e salvas em {arquivo_saida}")

if __name__ == '__main__':
    main()