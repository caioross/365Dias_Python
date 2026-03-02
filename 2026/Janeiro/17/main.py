"""
Script para verificar se uma pessoa atingiu a maioridade penal ou civil.
"""

from datetime import datetime

def calcular_idade(ano_nascimento):
    """
    Calcula a idade da pessoa com base no ano de nascimento.

    :param ano_nascimento: int - O ano de nascimento da pessoa.
    :return: int - A idade da pessoa.
    """
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def verificar_maioridade(idade):
    """
    Verifica se a pessoa atingiu a maioridade penal ou civil.

    :param idade: int - A idade da pessoa.
    :return: str - Uma mensagem informando a situação de maioridade.
    """
    maioridade_penal = 18
    maioridade_civil = 21

    if idade >= maioridade_civil:
        return "A pessoa é maior de idade civil e penal."
    elif idade >= maioridade_penal:
        return "A pessoa é maior de idade penal, mas não civil."
    else:
        return "A pessoa não é maior de idade."

def main():
    """
    Função principal que solicita o ano de nascimento e verifica a maioridade.
    """
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        idade = calcular_idade(ano_nascimento)
        resultado = verificar_maioridade(idade)
        print(resultado)
    except ValueError:
        print("Por favor, digite um ano de nascimento válido.")

if __name__ == '__main__':
    main()