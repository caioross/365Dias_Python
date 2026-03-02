import os

def remover_pastas_vazias(diretorio):
    """
    Remove todas as subpastas vazias dentro de um diretório.

    Args:
        diretorio (str): O caminho do diretório a ser verificado.
    """
    for root, dirs, files in os.walk(diretorio, topdown=False):
        for nome_pasta in dirs:
            caminho_pasta = os.path.join(root, nome_pasta)
            if not os.listdir(caminho_pasta):
                os.rmdir(caminho_pasta)
                print(f"Pasta removida: {caminho_pasta}")

def main():
    """
    Função principal que executa o script para remover pastas vazias.
    """
    diretorio = input("Digite o caminho do diretório a ser organizado: ")
    if not os.path.isdir(diretorio):
        print("O caminho especificado não é um diretório válido.")
        return

    remover_pastas_vazias(diretorio)
    print("Processo de remoção de pastas vazias concluído.")

if __name__ == '__main__':
    main()