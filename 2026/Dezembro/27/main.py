"""
gerador_metas_ano_novo.py

Interface interativa para definir objetivos para 2027 e salvar em um dashboard.
"""

import json

def obter_objetivo():
    """
    Solicita ao usuário que insira um objetivo para 2027.
    
    Returns:
        str: O objetivo inserido pelo usuário.
    """
    return input("Digite um objetivo para 2027: ")

def salvar_objetivo(objetivo):
    """
    Salva o objetivo em um arquivo JSON.
    
    Args:
        objetivo (str): O objetivo a ser salvo.
    """
    try:
        with open('objetivos_2027.json', 'r') as file:
            objetivos = json.load(file)
    except FileNotFoundError:
        objetivos = []
    
    objetivos.append(objetivo)
    
    with open('objetivos_2027.json', 'w') as file:
        json.dump(objetivos, file, indent=4)
    
    print("Objetivo salvo com sucesso!")

def exibir_objetivos():
    """
    Exibe todos os objetivos salvos em 2027.
    """
    try:
        with open('objetivos_2027.json', 'r') as file:
            objetivos = json.load(file)
            print("Objetivos para 2027:")
            for idx, objetivo in enumerate(objetivos, start=1):
                print(f"{idx}. {objetivo}")
    except FileNotFoundError:
        print("Nenhum objetivo encontrado.")

def main():
    """
    Função principal que executa o script.
    """
    while True:
        print("\nMenu:")
        print("1. Adicionar Novo Objetivo")
        print("2. Exibir Objetivos")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            objetivo = obter_objetivo()
            salvar_objetivo(objetivo)
        elif escolha == '2':
            exibir_objetivos()
        elif escolha == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()