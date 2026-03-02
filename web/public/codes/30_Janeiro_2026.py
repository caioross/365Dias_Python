"""
Script para gerar uma lista de compras. O usuário pode adicionar itens à lista,
e no final, a lista será salva em um arquivo de texto.
"""

def adicionar_item(item, lista):
    """
    Adiciona um item à lista de compras.

    :param item: O item a ser adicionado à lista.
    :param lista: A lista de compras onde o item será adicionado.
    """
    lista.append(item)

def salvar_lista_em_arquivo(lista, nome_arquivo):
    """
    Salva a lista de compras em um arquivo de texto.

    :param lista: A lista de compras a ser salva.
    :param nome_arquivo: O nome do arquivo onde a lista será salva.
    """
    with open(nome_arquivo, 'w') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")

def main():
    """
    Função principal que executa o script.
    """
    lista_compras = []
    print("Bem-vindo ao Gerador de Lista de Compras!")
    
    while True:
        item = input("Digite um item para adicionar à lista (ou 'sair' para terminar): ")
        if item.lower() == 'sair':
            break
        adicionar_item(item, lista_compras)
    
    nome_arquivo = input("Digite o nome do arquivo onde deseja salvar a lista: ")
    salvar_lista_em_arquivo(lista_compras, nome_arquivo)
    print(f"Lista de compras salva em {nome_arquivo}!")

if __name__ == '__main__':
    main()