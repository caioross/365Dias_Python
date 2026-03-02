"""
conversor_moedas_offline_fixo.py

Este script permite a conversão de valores entre moedas usando uma tabela de taxas fixas
salva em um arquivo local. As taxas de conversão são carregadas de um arquivo CSV e podem ser
usadas para converter valores entre diferentes moedas.

Uso:
    python conversor_moedas_offline_fixo.py <moeda_origem> <moeda_destino> <valor>

Exemplo:
    python conversor_moedas_offline_fixo.py USD EUR 100

"""

import csv
import sys

def carregar_taxas_de_conversao(arquivo):
    """
    Carrega as taxas de conversão de um arquivo CSV.

    Args:
        arquivo (str): O caminho para o arquivo CSV contendo as taxas de conversão.

    Returns:
        dict: Um dicionário com as taxas de conversão.
    """
    taxas = {}
    with open(arquivo, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            taxas[(row['moeda_origem'], row['moeda_destino'])] = float(row['taxa'])
    return taxas

def converter_moeda(taxas, moeda_origem, moeda_destino, valor):
    """
    Converte um valor de uma moeda para outra usando as taxas de conversão.

    Args:
        taxas (dict): O dicionário contendo as taxas de conversão.
        moeda_origem (str): A moeda de origem.
        moeda_destino (str): A moeda de destino.
        valor (float): O valor a ser convertido.

    Returns:
        float: O valor convertido.
    """
    chave = (moeda_origem, moeda_destino)
    if chave in taxas:
        return valor * taxas[chave]
    else:
        raise ValueError(f"Taxa de conversão de {moeda_origem} para {moeda_destino} não encontrada.")

def main():
    if len(sys.argv) != 4:
        print("Uso: python conversor_moedas_offline_fixo.py <moeda_origem> <moeda_destino> <valor>")
        sys.exit(1)

    moeda_origem = sys.argv[1]
    moeda_destino = sys.argv[2]
    try:
        valor = float(sys.argv[3])
    except ValueError:
        print("O valor deve ser um número.")
        sys.exit(1)

    taxas = carregar_taxas_de_conversao('taxas.csv')
    try:
        valor_convertido = converter_moeda(taxas, moeda_origem, moeda_destino, valor)
        print(f"{valor} {moeda_origem} é igual a {valor_convertido} {moeda_destino}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()