import random

def gerar_frase_motivacional():
    """
    Retorna uma frase inspiradora aleatória da lista de frases.
    
    Returns:
        str: Uma frase inspiradora.
    """
    frases = [
        "O sucesso é a soma de pequenos esforços repetidos dia após dia.",
        "Acredite em si mesmo e tudo será possível.",
        "O futuro pertence àqueles que acreditam na beleza de seus sonhos.",
        "Não espere por oportunidades, crie-as.",
        "Seja a mudança que você deseja ver no mundo.",
        "A vida é 10% o que acontece a você e 90% como você reage a isso.",
        "O maior risco é não arriscar nada.",
        "O sucesso é a capacidade de ir de fracasso a fracasso sem perder o entusiasmo.",
        "A única maneira de fazer um grande trabalho é amar o que você faz.",
        "O verdadeiro sucesso não é o sucesso da maioria, é ser você mesmo."
    ]
    return random.choice(frases)

def main():
    """
    Função principal que exibe uma frase motivacional aleatória.
    """
    frase = gerar_frase_motivacional()
    print(frase)

if __name__ == '__main__':
    main()