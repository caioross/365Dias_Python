from datetime import datetime, timedelta

def calcular_dias_ate_ano_novo():
    """
    Calcula quantos dias faltam para o próximo ano.

    Returns:
        int: Número de dias até o próximo ano.
    """
    hoje = datetime.now()
    proximo_ano = hoje.year + 1
    primeiro_de_ano = datetime(proximo_ano, 1, 1)
    dias_ate_ano_novo = (primeiro_de_ano - hoje).days
    return dias_ate_ano_novo

def exibir_boas_vindas():
    """
    Exibe uma mensagem de boas-vindas personalizada.
    """
    nome = input("Digite seu nome: ")
    print(f"Boas-vindas, {nome}! Pronto para um novo ano cheio de oportunidades.")

def main():
    """
    Função principal que executa o script.
    """
    exibir_boas_vindas()
    dias_ate_ano_novo = calcular_dias_ate_ano_novo()
    print(f"Faltam {dias_ate_ano_novo} dias para o próximo ano novo!")

if __name__ == '__main__':
    main()