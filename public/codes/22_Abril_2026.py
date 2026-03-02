import random

def gerar_senha_pronunciavel(tamanho=8):
    """
    Gera uma senha pronunciável de um tamanho especificado.
    
    Args:
        tamanho (int): O número de sílabas na senha. Default é 8.
        
    Returns:
        str: Uma senha pronunciável.
    """
    sílabas = [
        'ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du',
        'fa', 'fe', 'fi', 'fo', 'fu', 'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho', 'hu',
        'ja', 'je', 'ji', 'jo', 'ju', 'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu',
        'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu',
        'qa', 'qe', 'qi', 'qo', 'qu', 'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su',
        'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu', 'xa', 'xe', 'xi', 'xo', 'xu',
        'ya', 'ye', 'yi', 'yo', 'yu', 'za', 'ze', 'zi', 'zo', 'zu'
    ]
    
    senha = ''.join(random.choice(sílabas) for _ in range(tamanho))
    return senha

def main():
    """
    Função principal que gera uma senha pronunciável e a imprime.
    """
    tamanho_senha = 8  # Pode ser ajustado conforme necessário
    senha = gerar_senha_pronunciavel(tamanho_senha)
    print(f'Senha gerada: {senha}')

if __name__ == '__main__':
    main()