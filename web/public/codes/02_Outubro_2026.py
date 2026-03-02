"""
calculadora_calorias_diarias.py

Script para calcular a taxa metabólica basal (TMB) e as calorias necessárias
com base no nível de atividade do usuário.

Uso:
    python calculadora_calorias_diarias.py

Funções:
    - calcular_tmb_homens(peso, altura, idade)
    - calcular_tmb_mulheres(peso, altura, idade)
    - calcular_calorias_necessarias(tmb, nivel_atividade)
"""

def calcular_tmb_homens(peso, altura, idade):
    """
    Calcula a taxa metabólica basal para homens usando a fórmula de Harris-Benedict.

    Args:
        peso (float): Peso do indivíduo em quilogramas.
        altura (float): Altura do indivíduo em centímetros.
        idade (int): Idade do indivíduo em anos.

    Returns:
        float: Taxa metabólica basal em calorias por dia.
    """
    return 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)

def calcular_tmb_mulheres(peso, altura, idade):
    """
    Calcula a taxa metabólica basal para mulheres usando a fórmula de Harris-Benedict.

    Args:
        peso (float): Peso do indivíduo em quilogramas.
        altura (float): Altura do indivíduo em centímetros.
        idade (int): Idade do indivíduo em anos.

    Returns:
        float: Taxa metabólica basal em calorias por dia.
    """
    return 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)

def calcular_calorias_necessarias(tmb, nivel_atividade):
    """
    Calcula as calorias necessárias com base no nível de atividade.

    Args:
        tmb (float): Taxa metabólica basal em calorias por dia.
        nivel_atividade (str): Nível de atividade do indivíduo ('sedentario', 'leve', 'moderado', 'ativo', 'muito ativo').

    Returns:
        float: Calorias necessárias em calorias por dia.
    """
    fatores_atividade = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'ativo': 1.725,
        'muito ativo': 1.9
    }
    return tmb * fatores_atividade.get(nivel_atividade, 1.2)

def main():
    """
    Função principal do script para calcular a TMB e calorias necessárias.
    """
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em cm: "))
    idade = int(input("Digite a idade em anos: "))
    sexo = input("Digite o sexo (M/F): ").upper()
    nivel_atividade = input("Digite o nível de atividade (sedentario, leve, moderado, ativo, muito ativo): ").lower()

    if sexo == 'M':
        tmb = calcular_tmb_homens(peso, altura, idade)
    elif sexo == 'F':
        tmb = calcular_tmb_mulheres(peso, altura, idade)
    else:
        print("Sexo inválido. Use 'M' para masculino e 'F' para feminino.")
        return

    calorias_necessarias = calcular_calorias_necessarias(tmb, nivel_atividade)
    print(f"Taxa Metabólica Basal: {tmb:.2f} calorias/dia")
    print(f"Calorias Necessárias: {calorias_necessarias:.2f} calorias/dia")

if __name__ == '__main__':
    main()