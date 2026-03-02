import re

def is_valid_old_pattern(plate: str) -> bool:
    """
    Verifica se a placa segue o padrão antigo de placa brasileira (ABC-1234).
    
    :param plate: A placa a ser verificada.
    :return: True se a placa é válida no padrão antigo, False caso contrário.
    """
    pattern = re.compile(r'^[A-Z]{3}-\d{4}$')
    return bool(pattern.match(plate))

def is_valid_mercosul_pattern(plate: str) -> bool:
    """
    Verifica se a placa segue o padrão Mercosul de placa brasileira (ABC-1234).
    
    :param plate: A placa a ser verificada.
    :return: True se a placa é válida no padrão Mercosul, False caso contrário.
    """
    pattern = re.compile(r'^[A-Z]{3}\d[A-Z]\d{2}$')
    return bool(pattern.match(plate))

def check_plate(plate: str) -> str:
    """
    Verifica se a placa é válida no padrão antigo ou Mercosul.
    
    :param plate: A placa a ser verificada.
    :return: Uma string indicando o padrão da placa ou uma mensagem de erro.
    """
    plate = plate.upper()
    if is_valid_old_pattern(plate):
        return "A placa é válida no padrão antigo."
    elif is_valid_mercosul_pattern(plate):
        return "A placa é válida no padrão Mercosul."
    else:
        return "A placa é inválida."

def main():
    """
    Função principal que solicita ao usuário uma placa e verifica seu padrão.
    """
    plate = input("Digite a placa do veículo: ")
    result = check_plate(plate)
    print(result)

if __name__ == '__main__':
    main()