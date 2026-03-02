def get_matrix_input(rows, cols):
    """
    Solicita ao usuário que insira os elementos de uma matriz.

    :param rows: Número de linhas da matriz.
    :param cols: Número de colunas da matriz.
    :return: Uma lista de listas representando a matriz.
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    element = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")
        matrix.append(row)
    return matrix


def add_matrices(matrix1, matrix2):
    """
    Realiza a soma de duas matrizes.

    :param matrix1: Primeira matriz.
    :param matrix2: Segunda matriz.
    :return: Uma nova matriz resultante da soma.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


def print_matrix(matrix):
    """
    Imprime uma matriz de forma formatada.

    :param matrix: Matriz a ser impressa.
    """
    for row in matrix:
        print(" ".join(f"{element:.2f}" for element in row))


def main():
    """
    Função principal que executa o programa de soma de matrizes.
    """
    try:
        rows = int(input("Digite o número de linhas das matrizes: "))
        cols = int(input("Digite o número de colunas das matrizes: "))

        print("\nDigite os elementos da primeira matriz:")
        matrix1 = get_matrix_input(rows, cols)

        print("\nDigite os elementos da segunda matriz:")
        matrix2 = get_matrix_input(rows, cols)

        print("\nMatriz 1:")
        print_matrix(matrix1)

        print("\nMatriz 2:")
        print_matrix(matrix2)

        result_matrix = add_matrices(matrix1, matrix2)

        print("\nResultado da soma das matrizes:")
        print_matrix(result_matrix)

    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == '__main__':
    main()