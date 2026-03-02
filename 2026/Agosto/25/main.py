"""
Script para extrair tabelas de um PDF e carregá-las em um DataFrame do Pandas.
"""

import pandas as pd
from PyPDF2 import PdfReader
import tabula

def extrair_tabelas_do_pdf(pdf_path):
    """
    Extrai tabelas de um PDF e retorna uma lista de DataFrames.

    Args:
        pdf_path (str): Caminho para o arquivo PDF.

    Returns:
        list: Lista de DataFrames, cada um representando uma tabela extraída.
    """
    # Usa a biblioteca tabula para ler tabelas do PDF
    tabelas = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tabelas

def salvar_tabelas_em_csv(tabelas, output_dir):
    """
    Salva cada tabela em um arquivo CSV no diretório especificado.

    Args:
        tabelas (list): Lista de DataFrames a serem salvos.
        output_dir (str): Diretório onde os arquivos CSV serão salvos.
    """
    for i, tabela in enumerate(tabelas):
        file_name = f"{output_dir}/tabela_{i+1}.csv"
        tabela.to_csv(file_name, index=False)
        print(f"Tabela {i+1} salva como {file_name}")

def main():
    """
    Função principal que extrai tabelas de um PDF e salva-as como arquivos CSV.
    """
    pdf_path = 'caminho/para/seu/arquivo.pdf'  # Substitua pelo caminho do seu PDF
    output_dir = 'caminho/para/diretorio/saida'  # Substitua pelo diretório de saída

    # Extrai as tabelas do PDF
    tabelas = extrair_tabelas_do_pdf(pdf_path)

    # Salva as tabelas como arquivos CSV
    salvar_tabelas_em_csv(tabelas, output_dir)

if __name__ == '__main__':
    main()