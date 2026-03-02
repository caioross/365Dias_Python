"""
Script para conversão de unidades de armazenamento.
Suporta conversões entre Bytes, KB, MB, GB e TB.
"""

def bytes_to_kilobytes(bytes_value):
    """Converte bytes para kilobytes."""
    return bytes_value / 1024

def kilobytes_to_bytes(kilobytes_value):
    """Converte kilobytes para bytes."""
    return kilobytes_value * 1024

def bytes_to_megabytes(bytes_value):
    """Converte bytes para megabytes."""
    return bytes_value / (1024 ** 2)

def megabytes_to_bytes(megabytes_value):
    """Converte megabytes para bytes."""
    return megabytes_value * (1024 ** 2)

def bytes_to_gigabytes(bytes_value):
    """Converte bytes para gigabytes."""
    return bytes_value / (1024 ** 3)

def gigabytes_to_bytes(gigabytes_value):
    """Converte gigabytes para bytes."""
    return gigabytes_value * (1024 ** 3)

def bytes_to_terabytes(bytes_value):
    """Converte bytes para terabytes."""
    return bytes_value / (1024 ** 4)

def terabytes_to_bytes(terabytes_value):
    """Converte terabytes para bytes."""
    return terabytes_value * (1024 ** 4)

def convert(value, from_unit, to_unit):
    """
    Converte um valor de uma unidade de armazenamento para outra.
    
    :param value: Valor a ser convertido.
    :param from_unit: Unidade de origem ('B', 'KB', 'MB', 'GB', 'TB').
    :param to_unit: Unidade de destino ('B', 'KB', 'MB', 'GB', 'TB').
    :return: Valor convertido.
    """
    conversion_factors = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unidade de conversão inválida.")
    
    bytes_value = value * conversion_factors[from_unit]
    converted_value = bytes_value / conversion_factors[to_unit]
    return converted_value

def main():
    """Função principal para demonstrar o uso do conversor."""
    value = 1024
    from_unit = 'MB'
    to_unit = 'GB'
    
    try:
        result = convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} é igual a {result} {to_unit}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()