import os
from collections import defaultdict

def find_duplicate_files(directory):
    """
    Identifica arquivos duplicados com base no nome e tamanho.

    Args:
        directory (str): O diretório onde a busca será realizada.

    Returns:
        dict: Um dicionário onde as chaves são os nomes dos arquivos e os valores são listas de caminhos completos para arquivos com o mesmo nome e tamanho.
    """
    duplicates = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            key = (file, file_size)
            duplicates[key].append(file_path)
    
    # Filtrar apenas os arquivos que são duplicados
    return {key: paths for key, paths in duplicates.items() if len(paths) > 1}

def main():
    """
    Função principal que executa a busca por arquivos duplicados e imprime os resultados.
    """
    directory = input("Digite o diretório onde deseja procurar arquivos duplicados: ")
    duplicates = find_duplicate_files(directory)
    
    if duplicates:
        print("Arquivos duplicados encontrados:")
        for (file_name, _), paths in duplicates.items():
            print(f"Nome: {file_name}")
            for path in paths:
                print(f"  {path}")
    else:
        print("Nenhum arquivo duplicado encontrado.")

if __name__ == '__main__':
    main()