import pandas as pd
import sqlite3
from os import path

def import_excel_to_sqlite(excel_file, db_file):
    """
    Importa todas as abas de um arquivo Excel para tabelas em um banco de dados SQLite.

    :param excel_file: Caminho para o arquivo Excel.
    :param db_file: Caminho para o arquivo do banco de dados SQLite.
    """
    # Verifica se o arquivo Excel existe
    if not path.isfile(excel_file):
        raise FileNotFoundError(f"O arquivo Excel {excel_file} não foi encontrado.")

    # Carrega o arquivo Excel
    xls = pd.ExcelFile(excel_file)

    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect(db_file)

    try:
        # Itera sobre todas as abas no arquivo Excel
        for sheet_name in xls.sheet_names:
            # Lê a aba para um DataFrame
            df = pd.read_excel(xls, sheet_name=sheet_name)
            
            # Importa o DataFrame para uma tabela no banco de dados SQLite
            df.to_sql(sheet_name, conn, if_exists='replace', index=False)
            print(f"Tabela '{sheet_name}' importada com sucesso.")
    finally:
        # Fecha a conexão com o banco de dados
        conn.close()

def main():
    """
    Função principal que executa o script de importação de Excel para SQLite.
    """
    excel_file = 'dados.xlsx'  # Substitua pelo caminho do seu arquivo Excel
    db_file = 'banco_de_dados.db'  # Substitua pelo caminho do seu arquivo SQLite

    import_excel_to_sqlite(excel_file, db_file)

if __name__ == '__main__':
    main()