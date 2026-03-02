"""
simulador_vendas_pdv.py

Interface simples de "Ponto de Venda" para registrar itens e emitir cupom não fiscal.
"""

def registrar_item(itens, codigo, nome, preco):
    """
    Registra um item no PDV.

    :param itens: Dicionário onde os itens são armazenados.
    :param codigo: Código do item.
    :param nome: Nome do item.
    :param preco: Preço do item.
    """
    itens[codigo] = {'nome': nome, 'preco': preco}
    print(f"Item '{nome}' registrado com sucesso.")

def emitir_cupom(itens, carrinho):
    """
    Emite um cupom não fiscal com os itens do carrinho.

    :param itens: Dicionário com todos os itens registrados.
    :param carrinho: Lista de códigos dos itens no carrinho.
    """
    total = 0
    print("\n*** CUPOM NÃO FISCAL ***")
    for codigo in carrinho:
        if codigo in itens:
            item = itens[codigo]
            print(f"{item['nome']}: R$ {item['preco']:.2f}")
            total += item['preco']
        else:
            print(f"Item com código {codigo} não encontrado.")
    print(f"Total: R$ {total:.2f}")
    print("*** FIM DO CUPOM ***")

def main():
    """
    Função principal que executa o simulador de PDV.
    """
    itens = {}
    carrinho = []

    while True:
        print("\n1. Registrar Item")
        print("2. Adicionar Item ao Carrinho")
        print("3. Emitir Cupom")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Digite o código do item: ")
            nome = input("Digite o nome do item: ")
            preco = float(input("Digite o preço do item: "))
            registrar_item(itens, codigo, nome, preco)
        elif opcao == '2':
            codigo = input("Digite o código do item para adicionar ao carrinho: ")
            carrinho.append(codigo)
            print(f"Item com código {codigo} adicionado ao carrinho.")
        elif opcao == '3':
            emitir_cupom(itens, carrinho)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()