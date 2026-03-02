import csv
from datetime import datetime

def filter_adults(input_file, output_file):
    """
    Lê um arquivo CSV contendo informações de pessoas e gera um novo arquivo
    com apenas as pessoas maiores de 18 anos.

    Args:
        input_file (str): Caminho para o arquivo CSV de entrada.
        output_file (str): Caminho para o arquivo CSV de saída.
    """
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            birth_date = datetime.strptime(row['birth_date'], '%Y-%m-%d')
            age = (datetime.now() - birth_date).days // 365
            if age > 18:
                writer.writerow(row)

def main():
    input_file = 'pessoas.csv'
    output_file = 'maiores_18.csv'
    filter_adults(input_file, output_file)
    print(f"Arquivo '{output_file}' gerado com sucesso.")

if __name__ == '__main__':
    main()