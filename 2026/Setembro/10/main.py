"""
Extrator de Coordenadas EXIF

Este script extrai a latitude e longitude de uma foto a partir de seus metadados EXIF.
"""

import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image_path):
    """
    Obtém os dados EXIF de uma imagem.

    :param image_path: Caminho para o arquivo de imagem.
    :return: Um dicionário contendo os dados EXIF.
    """
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            return {TAGS.get(tag): value for tag, value in exif_data.items()} if exif_data else {}
    except IOError:
        print(f"Erro ao abrir o arquivo: {image_path}")
        return {}

def get_gps_info(exif_data):
    """
    Extrai informações GPS do dicionário de dados EXIF.

    :param exif_data: Dicionário contendo os dados EXIF.
    :return: Um dicionário contendo as informações GPS.
    """
    gps_info = {}
    if 'GPSInfo' in exif_data:
        for tag, value in exif_data['GPSInfo'].items():
            gps_info[GPSTAGS.get(tag)] = value
    return gps_info

def convert_to_degrees(value):
    """
    Converte os valores de coordenadas GPS para graus decimais.

    :param value: Tupla contendo os valores de coordenadas GPS.
    :return: Coordenada em graus decimais.
    """
    d = float(value[0][0]) / float(value[0][1])
    m = float(value[1][0]) / float(value[1][1])
    s = float(value[2][0]) / float(value[2][1])
    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(gps_info):
    """
    Obtém a latitude e longitude a partir das informações GPS.

    :param gps_info: Dicionário contendo as informações GPS.
    :return: Tupla contendo a latitude e longitude.
    """
    lat = None
    lon = None
    if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
        lat = convert_to_degrees(gps_info['GPSLatitude'])
        lon = convert_to_degrees(gps_info['GPSLongitude'])
        if gps_info['GPSLatitudeRef'] == 'S':
            lat = -lat
        if gps_info['GPSLongitudeRef'] == 'W':
            lon = -lon
    return lat, lon

def main():
    """
    Função principal que extrai e exibe as coordenadas GPS de uma imagem.
    """
    image_path = input("Digite o caminho para a imagem: ")
    if not os.path.exists(image_path):
        print("O arquivo não existe.")
        return

    exif_data = get_exif_data(image_path)
    gps_info = get_gps_info(exif_data)
    lat, lon = get_lat_lon(gps_info)

    if lat and lon:
        print(f"Latitude: {lat}, Longitude: {lon}")
    else:
        print("Não foram encontradas coordenadas GPS na imagem.")

if __name__ == '__main__':
    main()