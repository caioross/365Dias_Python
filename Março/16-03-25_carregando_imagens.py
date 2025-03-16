from PIL import Image

def exibir_imagem(caminho_imagem):
    """
    Função para carregar e exibir uma imagem.
    :param caminho_imagem: Caminho da imagem que será carregada.
    """
    try:
        # Carregar a imagem
        imagem = Image.open(caminho_imagem)
        
        # Exibir a imagem
        imagem.show()
        print(f"A imagem foi carregada e exibida com sucesso!")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_imagem}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao carregar ou exibir a imagem: {e}")

# Caminho da imagem
caminho_imagem = input("Digite o caminho da imagem para exibição: ")

# Exibir a imagem
exibir_imagem(caminho_imagem)
