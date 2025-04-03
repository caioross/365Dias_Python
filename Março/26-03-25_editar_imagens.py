from PIL import Image

def inverter_imagem(caminho_imagem):
    """
    Função para inverter a imagem horizontalmente.
    :param caminho_imagem: Caminho da imagem a ser invertida.
    """
    try:
        # Abre a imagem
        imagem = Image.open(caminho_imagem)
        
        # Inverte a imagem horizontalmente
        imagem_invertida = imagem.transpose(Image.FLIP_LEFT_RIGHT)
        
        # Exibe a imagem invertida
        imagem_invertida.show()
        
        # Salva a imagem invertida
        imagem_invertida.save("imagem_invertida.jpg")
        print("Imagem invertida salva como 'imagem_invertida.jpg'.")
    except Exception as e:
        print(f"Erro ao inverter a imagem: {e}")

def girar_imagem(caminho_imagem, angulo):
    """
    Função para girar a imagem em um determinado ângulo.
    :param caminho_imagem: Caminho da imagem a ser girada.
    :param angulo: Ângulo em graus para girar a imagem.
    """
    try:
        # Abre a imagem
        imagem = Image.open(caminho_imagem)
        
        # Gira a imagem
        imagem_girada = imagem.rotate(angulo)
        
        # Exibe a imagem girada
        imagem_girada.show()
        
        # Salva a imagem girada
        imagem_girada.save(f"imagem_girada_{angulo}.jpg")
        print(f"Imagem girada salva como 'imagem_girada_{angulo}.jpg'.")
    except Exception as e:
        print(f"Erro ao girar a imagem: {e}")

def redimensionar_imagem(caminho_imagem, largura, altura):
    """
    Função para redimensionar a imagem para as dimensões fornecidas.
    :param caminho_imagem: Caminho da imagem a ser redimensionada.
    :param largura: Nova largura da imagem.
    :param altura: Nova altura da imagem.
    """
    try:
        # Abre a imagem
        imagem = Image.open(caminho_imagem)
        
        # Redimensiona a imagem
        imagem_redimensionada = imagem.resize((largura, altura))
        
        # Exibe a imagem redimensionada
        imagem_redimensionada.show()
        
        # Salva a imagem redimensionada
        imagem_redimensionada.save(f"imagem_redimensionada_{largura}x{altura}.jpg")
        print(f"Imagem redimensionada salva como 'imagem_redimensionada_{largura}x{altura}.jpg'.")
    except Exception as e:
        print(f"Erro ao redimensionar a imagem: {e}")

def main():
    """
    Função principal para interagir com o usuário e realizar as manipulações na imagem.
    """
    caminho_imagem = input("Digite o caminho da imagem: ")

    # Opções de manipulação
    print("\nEscolha uma operação para a imagem:")
    print("1. Inverter a imagem")
    print("2. Girar a imagem")
    print("3. Redimensionar a imagem")
    
    escolha = int(input("Digite o número da operação desejada: "))
    
    if escolha == 1:
        inverter_imagem(caminho_imagem)
    elif escolha == 2:
        angulo = int(input("Digite o ângulo para girar a imagem (em graus): "))
        girar_imagem(caminho_imagem, angulo)
    elif escolha == 3:
        largura = int(input("Digite a nova largura da imagem: "))
        altura = int(input("Digite a nova altura da imagem: "))
        redimensionar_imagem(caminho_imagem, largura, altura)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
