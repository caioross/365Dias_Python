"""
calculo_tempo_leitura.py

Este script estima o tempo necessário para ler um texto com base na quantidade de palavras.
"""

def calcular_tempo_leitura(palavras, velocidade_media=200):
    """
    Calcula o tempo estimado para ler um texto.

    Args:
        palavras (int): O número de palavras no texto.
        velocidade_media (int, optional): A velocidade média de leitura em palavras por minuto. Padrão é 200.

    Returns:
        float: O tempo estimado em minutos para ler o texto.
    """
    if palavras <= 0:
        raise ValueError("O número de palavras deve ser maior que zero.")
    
    tempo_minutos = palavras / velocidade_media
    return tempo_minutos

def main():
    """
    Função principal que executa o script.
    Solicita ao usuário o número de palavras e exibe o tempo estimado para leitura.
    """
    try:
        palavras = int(input("Digite o número de palavras no texto: "))
        tempo = calcular_tempo_leitura(palavras)
        print(f"O tempo estimado para ler o texto é de {tempo:.2f} minutos.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()