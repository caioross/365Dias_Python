import matplotlib.pyplot as plt

def analisar_frequencia_letras(texto):
    """
    Analisa a frequência de cada letra em um texto fornecido.

    Args:
    texto (str): O texto para analisar.

    Returns:
    dict: Um dicionário com as letras como chaves e suas respectivas frequências como valores.
    """
    frequencia = {}
    for letra in texto.lower():
        if letra.isalpha():  # Considera apenas letras do alfabeto
            if letra in frequencia:
                frequencia[letra] += 1
            else:
                frequencia[letra] = 1
    return frequencia

def plotar_frequencia(frequencia):
    """
    Plota um gráfico de barras para visualizar a frequência de cada letra.

    Args:
    frequencia (dict): O dicionário contendo a frequência de cada letra.
    """
    letras = list(frequencia.keys())
    ocorrencias = list(frequencia.values())

    plt.figure(figsize=(10, 5))
    plt.bar(letras, ocorrencias, color='blue')
    plt.xlabel('Letras')
    plt.ylabel('Frequência')
    plt.title('Frequência de Letras no Texto')
    plt.show()

def main():
    """
    Função principal que executa o script.
    """
    texto = input("Digite o texto para analisar: ")
    frequencia = analisar_frequencia_letras(texto)
    plotar_frequencia(frequencia)

if __name__ == '__main__':
    main()