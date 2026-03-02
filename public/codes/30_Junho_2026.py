"""
Gerenciador de Biblioteca Pessoal

Este script permite ao usuário cadastrar livros lidos, autores e atribuir notas pessoais a esses livros.
"""

import json

class Livro:
    """Representa um livro com título, autor e nota pessoal."""
    
    def __init__(self, titulo, autor, nota):
        self.titulo = titulo
        self.autor = autor
        self.nota = nota

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', nota={self.nota})"

class Biblioteca:
    """Gerencia a coleção de livros lidos."""
    
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca."""
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def listar_livros(self):
        """Lista todos os livros na biblioteca."""
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            for livro in self.livros:
                print(livro)

    def salvar_biblioteca(self, arquivo):
        """Salva a biblioteca em um arquivo JSON."""
        livros_data = [{'titulo': livro.titulo, 'autor': livro.autor, 'nota': livro.nota} for livro in self.livros]
        with open(arquivo, 'w') as f:
            json.dump(livros_data, f, indent=4)
        print(f"Biblioteca salva em {arquivo}.")

    def carregar_biblioteca(self, arquivo):
        """Carrega a biblioteca de um arquivo JSON."""
        try:
            with open(arquivo, 'r') as f:
                livros_data = json.load(f)
                self.livros = [Livro(l['titulo'], l['autor'], l['nota']) for l in livros_data]
            print(f"Biblioteca carregada de {arquivo}.")
        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado.")

def main():
    """Função principal para interagir com o usuário."""
    biblioteca = Biblioteca()
    
    while True:
        print("\n1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Salvar Biblioteca")
        print("4. Carregar Biblioteca")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            nota = float(input("Digite a nota pessoal (0-10): "))
            livro = Livro(titulo, autor, nota)
            biblioteca.adicionar_livro(livro)
        elif escolha == '2':
            biblioteca.listar_livros()
        elif escolha == '3':
            arquivo = input("Digite o nome do arquivo para salvar: ")
            biblioteca.salvar_biblioteca(arquivo)
        elif escolha == '4':
            arquivo = input("Digite o nome do arquivo para carregar: ")
            biblioteca.carregar_biblioteca(arquivo)
        elif escolha == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()