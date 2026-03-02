import sqlite3
from typing import List, Tuple

def conectar_banco():
    """Conecta ao banco de dados SQLite e retorna a conexão e o cursor."""
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    """Cria a tabela de livros se ela não existir."""
    conn, cursor = conectar_banco()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            status_leitura TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_livro(titulo: str, autor: str, genero: str, status_leitura: str):
    """Adiciona um novo livro ao banco de dados."""
    conn, cursor = conectar_banco()
    cursor.execute('''
        INSERT INTO livros (titulo, autor, genero, status_leitura)
        VALUES (?, ?, ?, ?)
    ''', (titulo, autor, genero, status_leitura))
    conn.commit()
    conn.close()

def buscar_livros_por_autor(autor: str) -> List[Tuple]:
    """Busca livros pelo nome do autor."""
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM livros WHERE autor = ?', (autor,))
    livros = cursor.fetchall()
    conn.close()
    return livros

def buscar_livros_por_genero(genero: str) -> List[Tuple]:
    """Busca livros pelo gênero."""
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM livros WHERE genero = ?', (genero,))
    livros = cursor.fetchall()
    conn.close()
    return livros

def buscar_livros_por_status(status_leitura: str) -> List[Tuple]:
    """Busca livros pelo status de leitura."""
    conn, cursor = conectar_banco()
    cursor.execute('SELECT * FROM livros WHERE status_leitura = ?', (status_leitura,))
    livros = cursor.fetchall()
    conn.close()
    return livros

def main():
    """Função principal para executar o script."""
    criar_tabela()
    
    # Exemplo de adicionar livros
    adicionar_livro('1984', 'George Orwell', 'Distopia', 'Lido')
    adicionar_livro('Dom Quixote', 'Miguel de Cervantes', 'Ficção', 'Não Lido')
    
    # Exemplo de buscas
    print("Livros de George Orwell:")
    for livro in buscar_livros_por_autor('George Orwell'):
        print(livro)
    
    print("\nLivros de Ficção:")
    for livro in buscar_livros_por_genero('Ficção'):
        print(livro)
    
    print("\nLivros Lidos:")
    for livro in buscar_livros_por_status('Lido'):
        print(livro)

if __name__ == '__main__':
    main()