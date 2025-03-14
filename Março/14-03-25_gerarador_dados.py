import random
import string

def gerar_palavra(tamanho=5):
    """
    Função para gerar uma palavra aleatória de tamanho específico.
    :param tamanho: Número de caracteres na palavra.
    :return: Palavra gerada aleatoriamente.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=tamanho))

def gerar_numero(minimo=1, maximo=100):
    """
    Função para gerar um número aleatório entre o mínimo e o máximo.
    :param minimo: Limite inferior do número aleatório.
    :param maximo: Limite superior do número aleatório.
    :return: Número aleatório gerado.
    """
    return random.randint(minimo, maximo)

def gerar_frase():
    """
    Função para gerar uma frase aleatória composta por palavras e números.
    :return: Frase gerada aleatoriamente.
    """
    num_palavras = random.randint(3, 7)  # Frase entre 3 e 7 palavras
    frase = ' '.join(gerar_palavra(random.randint(3, 8)) for _ in range(num_palavras))
    return frase.capitalize() + '.'

def gerar_dados_aleatorios(quantidade_linhas=10):
    """
    Função para gerar um conjunto de dados aleatórios.
    :param quantidade_linhas: Quantidade de linhas a serem geradas no arquivo.
    :return: Lista de linhas com dados aleatórios.
    """
    dados = []
    for _ in range(quantidade_linhas):
        tipo_dado = random.choice(['numero', 'palavra', 'frase'])
        if tipo_dado == 'numero':
            dados.append(str(gerar_numero()))
        elif tipo_dado == 'palavra':
            dados.append(gerar_palavra())
        elif tipo_dado == 'frase':
            dados.append(gerar_frase())
    return dados

def salvar_arquivo(nome_arquivo='dados_aleatorios.txt', quantidade_linhas=10):
    """
    Função para salvar dados aleatórios em um arquivo de texto.
    :param nome_arquivo: Nome do arquivo a ser salvo.
    :param quantidade_linhas: Quantidade de linhas a serem geradas.
    """
    dados = gerar_dados_aleatorios(quantidade_linhas)
    
    with open(nome_arquivo, 'w') as f:
        for linha in dados:
            f.write(linha + '\n')
    
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso com {quantidade_linhas} linhas de dados aleatórios!")

# Executando a geração do arquivo
if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo (com extensão .txt): ")
    quantidade_linhas = int(input("Digite o número de linhas que o arquivo deve ter: "))
    salvar_arquivo(nome_arquivo, quantidade_linhas)
