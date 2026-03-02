import csv

def csv_to_markdown_table(csv_file_path, markdown_file_path):
    """
    Converte um arquivo CSV em uma tabela formatada para Markdown.

    Args:
        csv_file_path (str): Caminho para o arquivo CSV de entrada.
        markdown_file_path (str): Caminho para o arquivo Markdown de saída.
    """
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        rows = list(csv_reader)

    # Cria a primeira linha da tabela (headers)
    markdown_table = '| ' + ' | '.join(headers) + ' |\n'
    markdown_table += '| ' + ' | '.join(['---'] * len(headers)) + ' |\n'

    # Adiciona as linhas de dados
    for row in rows:
        markdown_table += '| ' + ' | '.join(row) + ' |\n'

    # Escreve a tabela Markdown em um arquivo
    with open(markdown_file_path, mode='w', encoding='utf-8') as markdown_file:
        markdown_file.write(markdown_table)

def main():
    """
    Função principal que executa o conversor de CSV para Markdown.
    """
    csv_file_path = 'data.csv'  # Caminho para o arquivo CSV de entrada
    markdown_file_path = 'README.md'  # Caminho para o arquivo Markdown de saída

    csv_to_markdown_table(csv_file_path, markdown_file_path)
    print(f"Tabela convertida com sucesso para {markdown_file_path}")

if __name__ == '__main__':
    main()