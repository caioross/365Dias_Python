import tkinter as tk
from tkinter import ttk
import sqlite3

# Função para conectar ao banco de dados e buscar os dados
def buscar_dados():
    try:
        # Conecta ao banco de dados SQLite (substitua pelo seu próprio banco de dados)
        conn = sqlite3.connect('seu_banco.db')
        cursor = conn.cursor()

        # Executa uma consulta SQL para buscar todos os dados de uma tabela (substitua 'tabela' pelo nome da sua tabela)
        cursor.execute("SELECT * FROM tabela")

        # Recupera os resultados da consulta
        dados = cursor.fetchall()

        # Limpa a árvore (se houver dados anteriores)
        for item in tree.get_children():
            tree.delete(item)

        # Insere os dados na árvore (visualização)
        for row in dados:
            tree.insert("", tk.END, values=row)

        # Fecha a conexão com o banco de dados
        conn.close()
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")

# Função para criar a interface gráfica
def criar_interface():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Visualização de Dados do Banco de Dados")

    # Cria um botão para buscar os dados do banco
    btn_buscar = tk.Button(janela, text="Buscar Dados", command=buscar_dados)
    btn_buscar.pack(pady=10)

    # Cria uma Treeview (árvore) para exibir os dados do banco
    global tree
    tree = ttk.Treeview(janela, columns=("ID", "Nome", "Idade", "Cidade"), show="headings")
    
    # Configura as colunas (substitua de acordo com os dados do seu banco)
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Idade", text="Idade")
    tree.heading("Cidade", text="Cidade")
    
    # Exibe as colunas na janela
    tree.pack(padx=10, pady=10)

    # Inicia a interface gráfica
    janela.mainloop()

# Função principal que chama a criação da interface
if __name__ == "__main__":
    criar_interface()
