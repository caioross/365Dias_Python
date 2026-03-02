import shutil

def check_disk_space(path):
    """
    Verifica o espaço livre em disco para a partição onde o caminho especificado reside.

    Args:
    path (str): Caminho no sistema de arquivos para verificar o espaço livre.

    Returns:
    float: Percentual de espaço livre na partição.
    """
    total, used, free = shutil.disk_usage(path)
    percent_free = (free / total) * 100
    return percent_free

def main():
    """
    Função principal que verifica o espaço livre em disco e exibe um aviso se for inferior a 10%.
    """
    path = '/'  # Verifica o espaço livre na partição raiz
    percent_free = check_disk_space(path)
    
    if percent_free < 10:
        print(f"ATENÇÃO: A partição {path} tem apenas {percent_free:.2f}% de espaço livre.")
    else:
        print(f"Espaço livre na partição {path}: {percent_free:.2f}%")

if __name__ == '__main__':
    main()