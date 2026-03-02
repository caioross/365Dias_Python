import json

def obter_preferencias_usuario():
    """
    Solicita ao usuário que insira suas preferências e retorna um dicionário com essas informações.
    """
    preferencias = {}
    preferencias['nome'] = input("Digite seu nome: ")
    preferencias['idade'] = int(input("Digite sua idade: "))
    preferencias['linguagem_preferida'] = input("Digite sua linguagem de programação preferida: ")
    preferencias['editor_de_codigo'] = input("Digite seu editor de código preferido: ")
    preferencias['sistema_operacional'] = input("Digite seu sistema operacional preferido: ")
    return preferencias

def criar_arquivo_config(preferencias, nome_arquivo='config.json'):
    """
    Cria um arquivo JSON com as preferências do usuário.
    
    :param preferencias: Dicionário contendo as preferências do usuário.
    :param nome_arquivo: Nome do arquivo JSON a ser criado.
    """
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(preferencias, arquivo, indent=4)
    print(f"Arquivo {nome_arquivo} criado com sucesso.")

def main():
    """
    Função principal que executa o script.
    """
    preferencias = obter_preferencias_usuario()
    criar_arquivo_config(preferencias)

if __name__ == '__main__':
    main()