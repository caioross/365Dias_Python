"""
calculo_frequencia_notas_musicais.py

Este script calcula a frequência em Hertz de uma nota musical baseada em sua oitava.
Utiliza a fórmula de Do4 (A4) = 440 Hz como referência.
"""

def calcular_frequencia(nota, oitava):
    """
    Calcula a frequência de uma nota musical em uma determinada oitava.

    Args:
        nota (str): A nota musical (por exemplo, 'C', 'D', 'E', 'F', 'G', 'A', 'B').
        oitava (int): A oitava da nota (por exemplo, 4, 5, 6).

    Returns:
        float: A frequência da nota em Hertz.
    """
    notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    frequencia_do4 = 440.0  # Frequência de A4 em Hz
    indice_do4 = notas.index('A')
    
    # Calcular o índice da nota desejada
    indice_nota = notas.index(nota)
    intervalo = indice_nota - indice_do4 + (oitava - 4) * 12
    
    # Calcular a frequência usando a fórmula
    frequencia = frequencia_do4 * (2 ** (intervalo / 12))
    
    return frequencia

def main():
    """
    Função principal que solicita ao usuário uma nota e uma oitava,
    e então calcula e exibe a frequência correspondente.
    """
    nota = input("Digite a nota musical (por exemplo, C, D, E, F, G, A, B): ").upper()
    try:
        oitava = int(input("Digite a oitava (por exemplo, 4, 5, 6): "))
        frequencia = calcular_frequencia(nota, oitava)
        print(f"A frequência de {nota}{oitava} é {frequencia:.2f} Hz.")
    except ValueError:
        print("Entrada inválida. Certifique-se de que a oitava é um número inteiro.")
    except ValueError as e:
        print(f"Nota inválida: {e}")

if __name__ == '__main__':
    main()