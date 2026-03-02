import sys

def generate_insert_statements(table_name, data_list):
    """
    Gera comandos SQL INSERT INTO a partir de uma lista de dicionários.

    Args:
        table_name (str): Nome da tabela para a qual os dados serão inseridos.
        data_list (list of dict): Lista de dicionários onde cada dicionário representa uma linha de dados.

    Returns:
        list of str: Lista de comandos SQL INSERT INTO.
    """
    if not data_list:
        return []

    # Obter os nomes das colunas a partir das chaves do primeiro dicionário
    columns = ', '.join(data_list[0].keys())
    insert_statements = []

    for data in data_list:
        # Converter os valores do dicionário em uma string formatada para SQL
        values = ', '.join([f"'{str(value).replace("'", "''")}'" if isinstance(value, str) else str(value) for value in data.values()])
        insert_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        insert_statements.append(insert_statement)

    return insert_statements

def main():
    """
    Função principal que demonstra o uso do gerador de comandos SQL INSERT INTO.
    """
    # Exemplo de dados
    data = [
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 25},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]

    # Nome da tabela
    table = 'users'

    # Gerar comandos SQL
    sql_statements = generate_insert_statements(table, data)

    # Imprimir os comandos SQL gerados
    for statement in sql_statements:
        print(statement)

if __name__ == '__main__':
    main()