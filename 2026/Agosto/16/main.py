"""
extrator_fotos_instagram_publico.py

Script para baixar fotos de um perfil público do Instagram.
Este script é apenas para fins de estudo de scraping e deve ser usado de acordo com as diretrizes de uso da API do Instagram.

Uso:
python extrator_fotos_instagram_publico.py <username>

Exemplo:
python extrator_fotos_instagram_publico.py username
"""

import os
import requests
from bs4 import BeautifulSoup
import sys

def download_photos(username):
    """
    Baixa as fotos de um perfil público do Instagram.

    Args:
        username (str): O nome de usuário do perfil do Instagram.

    Returns:
        None
    """
    base_url = f'https://www.instagram.com/{username}/'
    response = requests.get(base_url)
    
    if response.status_code != 200:
        print(f"Não foi possível acessar o perfil do Instagram: {username}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', {'type': 'text/javascript'})
    script_text = script_tag.string

    # Extract the JSON part from the script tag
    start_index = script_text.find('{')
    end_index = script_text.rfind('}') + 1
    json_data = script_text[start_index:end_index]

    # Load the JSON data
    import json
    data = json.loads(json_data)

    # Extract the photos
    photos = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

    # Create a directory for the photos
    if not os.path.exists(username):
        os.makedirs(username)

    # Download the photos
    for photo in photos:
        photo_url = photo['node']['display_url']
        photo_name = photo_url.split('/')[-1]
        photo_path = os.path.join(username, photo_name)
        
        with open(photo_path, 'wb') as file:
            file.write(requests.get(photo_url).content)
        
        print(f"Baixado: {photo_name}")

def main():
    """
    Função principal do script.
    """
    if len(sys.argv) != 2:
        print("Uso: python extrator_fotos_instagram_publico.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    download_photos(username)

if __name__ == '__main__':
    main()