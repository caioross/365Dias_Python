"""
gerador_histograma_terminal.py

Este script cria um gráfico de barras simples usando caracteres ASCII para representar dados numéricos.
"""

def gerar_histograma(dados, altura_maxima=10, caractere='*'):
    """
    Gera um histograma ASCII com base nos dados fornecidos.

    :param dados: Lista de inteiros representando os valores a serem plotados.
    :param altura_maxima: Altura máxima das barras do histograma.
    :param caractere: Caractere usado para desenhar as barras do histograma.
    :return: Nada, apenas imprime o histograma no terminal.
    """
    if not dados:
        print("Nenhum dado fornecido.")
        return

    max_value = max(dados)
    escala = altura_maxima / max_value

    for valor in dados:
        altura = int(valor * escala)
        barra = caractere * altura
        print(f"{valor:4} {barra}")

def main():
    """
    Função principal que executa o script.
    """
    dados = [10, 20, 30, 40, 50]
    print("Histograma:")
    gerar_histograma(dados)

if __name__ == '__main__':
    main()