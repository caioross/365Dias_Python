"""
conversor_unidades_pressao.py

Este script fornece funções para converter valores de pressão entre as unidades:
- bar
- psi (pounds per square inch)
- pascal (Pa)
- atmosfera (atm)

As funções são projetadas para serem chamadas individualmente ou em conjunto para realizar as conversões necessárias.
"""

def bar_to_psi(bar):
    """Converte pressão de bar para psi."""
    return bar * 14.5038

def bar_to_pascal(bar):
    """Converte pressão de bar para pascal."""
    return bar * 100000

def bar_to_atm(bar):
    """Converte pressão de bar para atmosfera."""
    return bar / 1.01325

def psi_to_bar(psi):
    """Converte pressão de psi para bar."""
    return psi / 14.5038

def psi_to_pascal(psi):
    """Converte pressão de psi para pascal."""
    return psi * 6894.76

def psi_to_atm(psi):
    """Converte pressão de psi para atmosfera."""
    return psi / 14.6959

def pascal_to_bar(pascal):
    """Converte pressão de pascal para bar."""
    return pascal / 100000

def pascal_to_psi(pascal):
    """Converte pressão de pascal para psi."""
    return pascal / 6894.76

def pascal_to_atm(pascal):
    """Converte pressão de pascal para atmosfera."""
    return pascal / 101325

def atm_to_bar(atm):
    """Converte pressão de atmosfera para bar."""
    return atm * 1.01325

def atm_to_psi(atm):
    """Converte pressão de atmosfera para psi."""
    return atm * 14.6959

def atm_to_pascal(atm):
    """Converte pressão de atmosfera para pascal."""
    return atm * 101325

def main():
    """Função principal para demonstrar o uso das funções de conversão."""
    value = 1  # Valor de exemplo para conversão

    print(f"{value} bar é igual a:")
    print(f"  {bar_to_psi(value)} psi")
    print(f"  {bar_to_pascal(value)} pascal")
    print(f"  {bar_to_atm(value)} atm")

    print(f"{value} psi é igual a:")
    print(f"  {psi_to_bar(value)} bar")
    print(f"  {psi_to_pascal(value)} pascal")
    print(f"  {psi_to_atm(value)} atm")

    print(f"{value} pascal é igual a:")
    print(f"  {pascal_to_bar(value)} bar")
    print(f"  {pascal_to_psi(value)} psi")
    print(f"  {pascal_to_atm(value)} atm")

    print(f"{value} atm é igual a:")
    print(f"  {atm_to_bar(value)} bar")
    print(f"  {atm_to_psi(value)} psi")
    print(f"  {atm_to_pascal(value)} pascal")

if __name__ == '__main__':
    main()