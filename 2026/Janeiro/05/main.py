import random

def lancar_dado():
    """
    Simula o lançamento de um dado de 6 faces.
    
    Returns:
        int: Um número entre 1 e 6, simulando o resultado do lançamento do dado.
    """
    return random.randint(1, 6)

def main():
    """
    Função principal que controla o fluxo do jogo de lançamento de dados.
    """
    while True:
        input("Pressione Enter para lançar o dado...")
        resultado = lancar_dado()
        print(f"O dado caiu no número: {resultado}")
        
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == '__main__':
    main()