import sqlite3
from typing import List, Tuple

class Nota:
    """
    Classe que representa uma nota.
    """
    def __init__(self, id: int, conteudo: str):
        self.id = id
        self.conteudo = conteudo

    def __repr__(self):
        return f"Nota(id={self.id}, conteudo='{self.conteudo}')"

class GerenciadorAnotacoes:
    """
    Classe que gerencia as anotações em um banco de dados SQLite.
    """
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conectar_db()

    def conectar_db(self):
        """
        Conecta ao banco de dados SQLite.
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        """
        Cria a tabela de notas se ela não existir.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conteudo TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def adicionar_nota(self, conteudo: str) -> int:
        """
        Adiciona uma nova nota ao banco de dados.

        :param conteudo: O conteúdo da nota.
        :return: O ID da nota inserida.
        """
        self.cursor.execute('INSERT INTO notas (conteudo) VALUES (?)', (conteudo,))
        self.conn.commit()
        return self.cursor.lastrowid

    def obter_notas(self) -> List[Nota]:
        """
        Obtém todas as notas do banco de dados.

        :return: Uma lista de objetos Nota.
        """
        self.cursor.execute('SELECT id, conteudo FROM notas')
        rows = self.cursor.fetchall()
        return [Nota(id, conteudo) for id, conteudo in rows]

    def deletar_nota(self, nota_id: int):
        """
        Deleta uma nota do banco de dados.

        :param nota_id: O ID da nota a ser deletada.
        """
        self.cursor.execute('DELETE FROM notas WHERE id = ?', (nota_id,))
        self.conn.commit()

    def fechar_conexao(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.conn.close()

def main():
    """
    Função principal que demonstra o uso do GerenciadorAnotacoes.
    """
    gerenciador = GerenciadorAnotacoes('notas.db')

    # Adicionar notas
    nota_id1 = gerenciador.adicionar_nota('Minha primeira nota')
    nota_id2 = gerenciador.adicionar_nota('Minha segunda nota')

    # Obter e imprimir todas as notas
    notas = gerenciador.obter_notas()
    print("Notas atuais:")
    for nota in notas:
        print(nota)

    # Deletar uma nota
    gerenciador.deletar_nota(nota_id1)

    # Obter e imprimir todas as notas novamente
    notas = gerenciador.obter_notas()
    print("\nNotas após a exclusão:")
    for nota in notas:
        print(nota)

    # Fechar a conexão com o banco de dados
    gerenciador.fechar_conexao()

if __name__ == '__main__':
    main()