import json
from jsonschema import validate, ValidationError

def load_json(file_path):
    """
    Carrega um arquivo JSON e retorna seu conteúdo como um dicionário.

    :param file_path: Caminho para o arquivo JSON.
    :return: Dicionário contendo o conteúdo do arquivo JSON.
    :raises FileNotFoundError: Se o arquivo não for encontrado.
    :raises json.JSONDecodeError: Se o arquivo não for um JSON válido.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def validate_json(data, schema):
    """
    Valida os dados JSON contra um schema JSON.

    :param data: Dados JSON a serem validados.
    :param schema: Schema JSON a ser usado para validação.
    :raises ValidationError: Se os dados não seguirem o schema.
    """
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise ValidationError(f"JSON validation error: {e.message}")

def main():
    """
    Função principal que carrega um arquivo JSON e valida-o contra um schema JSON.
    """
    json_file = 'data.json'
    schema_file = 'schema.json'

    try:
        data = load_json(json_file)
        schema = load_json(schema_file)
        validate_json(data, schema)
        print("O JSON é válido.")
    except (FileNotFoundError, json.JSONDecodeError, ValidationError) as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()