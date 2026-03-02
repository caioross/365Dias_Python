"""
tradutor_codigo_morse.py

Este script converte frases em texto comum para código Morse usando pontos e traços.
"""

def texto_para_morse(texto):
    """
    Converte um texto em código Morse.

    Args:
        texto (str): O texto a ser convertido para Morse.

    Returns:
        str: O texto convertido em código Morse.
    """
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
        '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
    }

    morse = ''
    for char in texto.upper():
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + ' '
        else:
            morse += char + ' '  # Mantém o caractere original se não for encontrado no dicionário

    return morse.strip()

def main():
    """
    Função principal que solicita ao usuário um texto e imprime o código Morse correspondente.
    """
    texto = input("Digite o texto que deseja converter para código Morse: ")
    morse = texto_para_morse(texto)
    print(f"Código Morse: {morse}")

if __name__ == '__main__':
    main()