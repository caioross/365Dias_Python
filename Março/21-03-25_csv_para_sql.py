import sqlite3
import csv

def conectar_banco():
    """
    Função para conectar ao banco de dados SQLite.
    Se o banco não existir, ele será criado.
    """
    conn = sqlite3.connect('dados.db')  # Nome do banco de dados SQLite
    return conn

def criar_tabela(conn):
    """
    Função para criar uma tabela no banco de dados, caso não exista.
    Ajuste os nomes das colunas de acordo com seu CSV.
    """
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_csv (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            email TEXT
        );
    ''')
    conn.commit()

def inserir_dados_csv(conn, csv_file):
    """
    Função para ler um arquivo CSV e inserir os dados na tabela SQL.
    :param conn: Conexão com o banco de dados.
    :param csv_file: Caminho do arquivo CSV a ser lido.
    """
    cursor = conn.cursor()
    
    # Abre o arquivo CSV para leitura
    with open(csv_file, mode='r', encoding='utf-8') as file:
        leitor_csv = csv.reader(file)
        
        # Pula a primeira linha (cabeçalho) do CSV
        next(leitor_csv)
        
        # Insere os dados do CSV na tabela
        for linha in leitor_csv:
            cursor.execute('''
                INSERT INTO dados_csv (nome, idade, email) 
                VALUES (?, ?, ?);
            ''', (linha[0], linha[1], linha[2]))
    
    conn.commit()

def exibir_dados(conn):
    """
    Função para exibir os dados da tabela SQL.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados_csv")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    """
    Função principal para executar o fluxo completo.
    """
    # Conectar ao banco de dados
    conn = conectar_banco()
    
    # Criar a tabela (caso não exista)
    criar_tabela(conn)
    
    # Caminho do arquivo CSV (substitua pelo caminho do seu arquivo CSV)
    caminho_csv = 'dados.csv'
    
    # Inserir dados do CSV na tabela SQL
    inserir_dados_csv(conn, caminho_csv)
    
    # Exibir os dados inseridos
    print("\nDados inseridos na tabela:")
    exibir_dados(conn)
    
    # Fechar a conexão
    conn.close()

if __name__ == "__main__":
    main()
