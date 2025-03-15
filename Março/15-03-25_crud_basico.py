import sqlite3

# Função para conectar ao banco de dados
def conectar_bd(nome_bd="exemplo.db"):
    """
    Função para conectar ao banco de dados SQLite.
    :param nome_bd: Nome do banco de dados (se não existir, será criado).
    :return: Conexão com o banco de dados.
    """
    return sqlite3.connect(nome_bd)

# Função para criar a tabela de usuários
def criar_tabela(conn):
    """
    Função para criar uma tabela de usuários.
    :param conn: Conexão com o banco de dados.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER
            )
        ''')
        conn.commit()
        print("Tabela 'usuarios' criada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")

# Função para adicionar um novo usuário
def adicionar_usuario(conn, nome, idade):
    """
    Função para adicionar um novo usuário na tabela.
    :param conn: Conexão com o banco de dados.
    :param nome: Nome do usuário.
    :param idade: Idade do usuário.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, idade) 
            VALUES (?, ?)
        ''', (nome, idade))
        conn.commit()
        print(f"Usuário '{nome}' adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar usuário: {e}")

# Função para listar todos os usuários
def listar_usuarios(conn):
    """
    Função para listar todos os usuários.
    :param conn: Conexão com o banco de dados.
    :return: Lista de usuários.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Idade: {usuario[2]}")
    except sqlite3.Error as e:
        print(f"Erro ao listar usuários: {e}")

# Função para atualizar um usuário
def atualizar_usuario(conn, id_usuario, novo_nome, nova_idade):
    """
    Função para atualizar os dados de um usuário.
    :param conn: Conexão com o banco de dados.
    :param id_usuario: ID do usuário a ser atualizado.
    :param novo_nome: Novo nome do usuário.
    :param nova_idade: Nova idade do usuário.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE usuarios 
            SET nome = ?, idade = ? 
            WHERE id = ?
        ''', (novo_nome, nova_idade, id_usuario))
        conn.commit()
        print(f"Usuário com ID {id_usuario} atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar usuário: {e}")

# Função para deletar um usuário
def deletar_usuario(conn, id_usuario):
    """
    Função para deletar um usuário.
    :param conn: Conexão com o banco de dados.
    :param id_usuario: ID do usuário a ser deletado.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM usuarios WHERE id = ?
        ''', (id_usuario,))
        conn.commit()
        print(f"Usuário com ID {id_usuario} deletado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao deletar usuário: {e}")

# Função principal que executa o CRUD
def menu():
    """
    Função que exibe o menu e permite a interação com o CRUD.
    """
    conn = conectar_bd()
    criar_tabela(conn)

    while True:
        print("\nMenu CRUD - SQLite")
        print("1. Adicionar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        
        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == '1':
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            adicionar_usuario(conn, nome, idade)
        elif escolha == '2':
            listar_usuarios(conn)
        elif escolha == '3':
            id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
            novo_nome = input("Digite o novo nome: ")
            nova_idade = int(input("Digite a nova idade: "))
            atualizar_usuario(conn, id_usuario, novo_nome, nova_idade)
        elif escolha == '4':
            id_usuario = int(input("Digite o ID do usuário a ser deletado: "))
            deletar_usuario(conn, id_usuario)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Escolha inválida! Por favor, tente novamente.")

    conn.close()

if __name__ == "__main__":
    menu()
