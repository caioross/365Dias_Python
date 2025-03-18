from captcha.image import ImageCaptcha
import random
import string

def gerar_captcha(texto=None, tamanho=200, altura=50, nome_arquivo="captcha.png"):
    """
    Função para gerar uma imagem de CAPTCHA.
    :param texto: Texto que será exibido no CAPTCHA. Se não fornecido, será gerado aleatoriamente.
    :param tamanho: Largura da imagem do CAPTCHA.
    :param altura: Altura da imagem do CAPTCHA.
    :param nome_arquivo: Nome do arquivo para salvar o CAPTCHA gerado.
    """
    # Caso o texto não seja fornecido, gera um texto aleatório de 6 caracteres
    if not texto:
        texto = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Cria um objeto ImageCaptcha
    captcha = ImageCaptcha(width=tamanho, height=altura)

    # Gera a imagem do CAPTCHA com o texto fornecido
    imagem_captcha = captcha.generate_image(texto)

    # Salva a imagem gerada em um arquivo
    imagem_captcha.save(nome_arquivo)

    print(f"CAPTCHA gerado com sucesso! Arquivo salvo como '{nome_arquivo}'")

if __name__ == "__main__":
    # Solicita ao usuário o texto para o CAPTCHA ou usa o padrão aleatório
    texto_captcha = input("Digite o texto para o CAPTCHA (deixe em branco para gerar aleatoriamente): ")
    nome_arquivo = input("Digite o nome do arquivo para salvar o CAPTCHA (exemplo: captcha.png): ")

    # Gera o CAPTCHA
    gerar_captcha(texto=texto_captcha if texto_captcha else None, nome_arquivo=nome_arquivo)
