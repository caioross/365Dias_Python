def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso (float): Peso do indivíduo em quilogramas.
        altura (float): Altura do indivíduo em metros.

    Returns:
        float: O valor do IMC.
    """
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero.")
    return peso / (altura ** 2)

def classificar_imc(imc):
    """
    Classifica o IMC de acordo com a Organização Mundial da Saúde (OMS).

    Args:
        imc (float): O valor do IMC.

    Returns:
        str: A classificação do IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    """
    Função principal que solicita ao usuário o peso e altura, calcula o IMC e classifica a saúde.
    """
    try:
        peso = float(input("Digite o peso em quilogramas: "))
        altura = float(input("Digite a altura em metros: "))

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()