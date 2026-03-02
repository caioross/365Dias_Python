def calcular_media(notas):
    """
    Calcula a média das notas fornecidas.

    :param notas: Uma lista contendo as quatro notas do aluno.
    :return: A média das notas.
    """
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    """
    Verifica se o aluno foi aprovado ou está em recuperação.

    :param media: A média das notas do aluno.
    :return: Uma string informando se o aluno foi aprovado ou está em recuperação.
    """
    if media >= 7:
        return "Aluno aprovado!"
    else:
        return "Aluno em recuperação."

def main():
    """
    Função principal que recebe as notas, calcula a média e verifica a situação do aluno.
    """
    try:
        notas = []
        for i in range(4):
            nota = float(input(f"Digite a nota {i + 1}: "))
            if nota < 0 or nota > 10:
                raise ValueError("Nota inválida. As notas devem estar entre 0 e 10.")
            notas.append(nota)

        media = calcular_media(notas)
        print(f"Média: {media:.2f}")
        print(verificar_aprovacao(media))

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()