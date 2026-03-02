import sys
import pkg_resources

def verificar_versao_python():
    """
    Verifica a versão do interpretador Python atualmente em uso.
    
    Returns:
        str: A versão do Python.
    """
    return sys.version

def listar_bibliotecas_instaladas():
    """
    Lista todas as bibliotecas (pacotes) instaladas no ambiente Python atual.
    
    Returns:
        list: Uma lista de nomes de pacotes instalados.
    """
    return [package.key for package in pkg_resources.working_set]

def main():
    """
    Função principal que executa a verificação da versão do Python e a listagem das bibliotecas instaladas.
    """
    versao_python = verificar_versao_python()
    print(f"Versão do Python: {versao_python}")
    
    bibliotecas = listar_bibliotecas_instaladas()
    print("\nBibliotecas instaladas:")
    for biblioteca in bibliotecas:
        print(biblioteca)

if __name__ == '__main__':
    main()