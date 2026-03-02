"""
gerador_playlist_spotify_humor.py

Script que sugere músicas baseadas no sentimento extraído de uma frase digitada pelo usuário.
Utiliza a API do Spotify para buscar músicas e a biblioteca TextBlob para analisar o sentimento da frase.
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from textblob import TextBlob

# Configuração das credenciais do Spotify
SPOTIFY_CLIENT_ID = 'your_client_id'
SPOTIFY_CLIENT_SECRET = 'your_client_secret'

def analisar_sentimento(frase):
    """
    Analisa o sentimento de uma frase usando a biblioteca TextBlob.

    Args:
        frase (str): A frase para análise de sentimento.

    Returns:
        str: O sentimento da frase ('positive', 'negative' ou 'neutral').
    """
    blob = TextBlob(frase)
    polaridade = blob.sentiment.polarity

    if polaridade > 0:
        return 'positive'
    elif polaridade < 0:
        return 'negative'
    else:
        return 'neutral'

def buscar_musicas_por_sentimento(sentimento):
    """
    Busca músicas no Spotify baseadas no sentimento fornecido.

    Args:
        sentimento (str): O sentimento para filtrar as músicas ('positive', 'negative' ou 'neutral').

    Returns:
        list: Uma lista de nomes de músicas que correspondem ao sentimento.
    """
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))
    query = f"genre:music {sentimento}"
    results = sp.search(q=query, type='track', limit=10)
    musicas = [track['name'] for track in results['tracks']['items']]
    return musicas

def main():
    """
    Função principal do script.
    Solicita ao usuário uma frase, analisa o sentimento e sugere músicas correspondentes.
    """
    frase = input("Digite uma frase para gerar uma playlist de humor: ")
    sentimento = analisar_sentimento(frase)
    print(f"Sentimento detectado: {sentimento}")
    
    musicas = buscar_musicas_por_sentimento(sentimento)
    print("Músicas sugeridas:")
    for musica in musicas:
        print(musica)

if __name__ == '__main__':
    main()