import csv
import json

def csv_to_json(csv_file_path, json_file_path, key_mapping):
    """
    Converte um arquivo CSV para um formato JSON com chaves personalizadas.

    :param csv_file_path: Caminho para o arquivo CSV de entrada.
    :param json_file_path: Caminho para o arquivo JSON de saída.
    :param key_mapping: Dicionário que mapeia as chaves do CSV para as chaves do JSON.
    """
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = []
            for row in csv_reader:
                # Mapeia as chaves do CSV para as chaves personalizadas
                mapped_row = {key_mapping.get(k, k): v for k, v in row.items()}
                data.append(mapped_row)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"Dados convertidos com sucesso de {csv_file_path} para {json_file_path}")

    except FileNotFoundError:
        print(f"O arquivo {csv_file_path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    """
    Função principal do script.
    """
    csv_file_path = 'input.csv'  # Caminho para o arquivo CSV de entrada
    json_file_path = 'output.json'  # Caminho para o arquivo JSON de saída
    key_mapping = {
        'Nome': 'name',
        'Idade': 'age',
        'Email': 'email'
    }  # Mapeamento personalizado de chaves

    csv_to_json(csv_file_path, json_file_path, key_mapping)

if __name__ == '__main__':
    main()