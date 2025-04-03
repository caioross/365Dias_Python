import re

def validar_cpf(cpf: str) -> bool:
    """
    Função para validar um CPF.
    :param cpf: CPF a ser validado (como string).
    :return: True se for válido, False se não for válido.
    """
    # Remover caracteres não numéricos (ex: pontos e traços)
    cpf = re.sub(r'\D', '', cpf)

    # Verificar se tem o comprimento correto
    if len(cpf) != 11:
        return False

    # Validar se todos os números são iguais (exemplo: 111.111.111.11)
    if cpf == cpf[0] * 11:
        return False

    # Validar os dois dígitos verificadores do CPF
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    digito1 = calcular_digito(cpf, peso1)
    digito2 = calcular_digito(cpf, peso2)

    return cpf[-2:] == f'{digito1}{digito2}'

def validar_cnpj(cnpj: str) -> bool:
    """
    Função para validar um CNPJ.
    :param cnpj: CNPJ a ser validado (como string).
    :return: True se for válido, False se não for válido.
    """
    # Remover caracteres não numéricos (ex: pontos, barra e traço)
    cnpj = re.sub(r'\D', '', cnpj)

    # Verificar se tem o comprimento correto
    if len(cnpj) != 14:
        return False

    # Validar se todos os números são iguais (exemplo: 111.111.111/1111-11)
    if cnpj == cnpj[0] * 14:
        return False

    # Função auxiliar para calcular o dígito verificador
    def calcular_digito(cnpj, peso):
        soma = sum(int(cnpj[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    digito1 = calcular_digito(cnpj, peso1)
    digito2 = calcular_digito(cnpj, peso2)

    return cnpj[-2:] == f'{digito1}{digito2}'

def validar_documento(documento: str) -> str:
    """
    Função para validar CPF ou CNPJ, identificando o tipo.
    :param documento: CPF ou CNPJ a ser validado.
    :return: Mensagem de erro ou sucesso.
    """
    if len(documento) == 11:
        if validar_cpf(documento):
            return "CPF válido."
        else:
            return "CPF inválido."
    elif len(documento) == 14:
        if validar_cnpj(documento):
            return "CNPJ válido."
        else:
            return "CNPJ inválido."
    else:
        return "Documento inválido. Deve ser um CPF ou CNPJ."

# Exemplos de uso:
documento = input("Digite o CPF ou CNPJ: ")
print(validar_documento(documento))
