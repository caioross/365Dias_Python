"""
conversor_yaml_para_json.py

Ferramenta de linha de comando para converter arquivos de configuração YAML em JSON.
"""

import argparse
import json
import yaml

def converter_yaml_para_json(caminho_yaml, caminho_json):
    """
    Converte um arquivo YAML para JSON.

    Args:
        caminho_yaml (str): Caminho para o arquivo YAML de entrada.
        caminho_json (str): Caminho para o arquivo JSON de saída.
    """
    try:
        with open(caminho_yaml, 'r', encoding='utf-8') as arquivo_yaml:
            dados = yaml.safe_load(arquivo_yaml)
        
        with open(caminho_json, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
        
        print(f"Arquivo YAML convertido com sucesso para {caminho_json}")
    except FileNotFoundError:
        print(f"Erro: O arquivo YAML '{caminho_yaml}' não foi encontrado.")
    except yaml.YAMLError as exc:
        print(f"Erro ao processar o arquivo YAML: {exc}")
    except Exception as exc:
        print(f"Erro inesperado: {exc}")

def main():
    """
    Função principal do script.
    """
    parser = argparse.ArgumentParser(description='Converte um arquivo YAML para JSON.')
    parser.add_argument('caminho_yaml', type=str, help='Caminho para o arquivo YAML de entrada.')
    parser.add_argument('caminho_json', type=str, help='Caminho para o arquivo JSON de saída.')

    args = parser.parse_args()
    converter_yaml_para_json(args.caminho_yaml, args.caminho_json)

if __name__ == '__main__':
    main()