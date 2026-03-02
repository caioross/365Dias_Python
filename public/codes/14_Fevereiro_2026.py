import os
import shutil
import tempfile

def limpar_cache_temporario():
    """
    Limpa a pasta de arquivos temporários do sistema operacional.
    
    Esta função localiza e apaga todos os arquivos e diretórios
    dentro da pasta de arquivos temporários do sistema operacional
    para liberar espaço.
    """
    temp_dir = tempfile.gettempdir()
    try:
        for root, dirs, files in os.walk(temp_dir, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.remove(file_path)
                    print(f"Arquivo removido: {file_path}")
                except Exception as e:
                    print(f"Erro ao remover arquivo {file_path}: {e}")
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Diretório removido: {dir_path}")
                except Exception as e:
                    print(f"Erro ao remover diretório {dir_path}: {e}")
        print("Limpeza de cache temporário concluída.")
    except Exception as e:
        print(f"Erro ao acessar diretório temporário {temp_dir}: {e}")

def main():
    """
    Função principal do script.
    
    Esta função chama a função de limpeza de cache temporário.
    """
    limpar_cache_temporario()

if __name__ == '__main__':
    main()