"""
gerador_tabuada_completa.py

Este script gera e salva em um arquivo .txt as tabuadas do 1 ao 10.
"""

def gerar_tabuada():
    """
    Gera as tabuadas do 1 ao 10.

    Returns:
        str: Uma string contendo todas as tabuadas.
    """
    tabuadas = []
    for i in range(1, 11):
        tabuada = f"Tabuada do {i}:\n"
        for j in range(1, 11):
            tabuada += f"{i} x {j} = {i * j}\n"
        tabuadas.append(tabuada)
        tabuadas.append("\n")
    return "".join(tabuadas)

def salvar_tabuadas_em_arquivo():
    """
    Gera as tabuadas e salva-as em um arquivo .txt.
    """
    tabuadas = gerar_tabuada()
    with open("tabuadas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(tabuadas)

def main():
    """
    Função principal que chama a função para salvar as tabuadas em arquivo.
    """
    salvar_tabuadas_em_arquivo()
    print("Tabuadas salvas em 'tabuadas.txt'.")

if __name__ == '__main__':
    main()