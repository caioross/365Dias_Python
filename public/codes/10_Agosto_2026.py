"""
conversor_json_para_yaml.py

Um utilitário simples para converter arquivos de configuração do formato JSON para YAML.
"""

import json
import yaml
import sys

def converter_json_para_yaml(json_file_path, yaml_file_path):
    """
    Converte um arquivo JSON para um arquivo YAML.

    Args:
        json_file_path (str): O caminho para o arquivo JSON de entrada.
        yaml_file_path (str): O caminho para o arquivo YAML de saída.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        with open(yaml_file_path, 'w', encoding='utf-8') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
        
        print(f"Arquivo JSON convertido com sucesso para {yaml_file_path}")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {json_file_path} não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {json_file_path} não é um JSON válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def main():
    """
    Função principal que executa o conversor de JSON para YAML.
    """
    if len(sys.argv) != 3:
        print("Uso: python conversor_json_para_yaml.py <caminho_do_arquivo_json> <caminho_do_arquivo_yaml>")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    yaml_file_path = sys.argv[2]
    
    converter_json_para_yaml(json_file_path, yaml_file_path)

if __name__ == '__main__':
    main()