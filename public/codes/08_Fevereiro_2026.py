import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    """
    Converte um arquivo JSON para um arquivo CSV.

    Args:
        json_file_path (str): O caminho para o arquivo JSON de entrada.
        csv_file_path (str): O caminho para o arquivo CSV de saída.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Verifica se os dados são uma lista de dicionários
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("O arquivo JSON deve conter uma lista de objetos (dicionários).")
        
        # Obtém os cabeçalhos do CSV a partir das chaves do primeiro dicionário
        headers = data[0].keys()
        
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(data)
        
        print(f"Conversão concluída. O arquivo CSV foi salvo em {csv_file_path}.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {json_file_path} não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {json_file_path} não é um JSON válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def main():
    """
    Função principal que executa o script de conversão de JSON para CSV.
    """
    json_file_path = 'dados.json'  # Caminho para o arquivo JSON de entrada
    csv_file_path = 'dados.csv'    # Caminho para o arquivo CSV de saída
    
    json_to_csv(json_file_path, csv_file_path)

if __name__ == '__main__':
    main()