from gtts import gTTS
import os

def texto_para_audio(texto, arquivo_saida="saida.mp3", idioma="pt"):
    """
    Função para converter texto em áudio (Text to Speech) usando gTTS.
    :param texto: Texto a ser convertido em áudio.
    :param arquivo_saida: Nome do arquivo de saída (padrão: 'saida.mp3').
    :param idioma: Idioma do áudio (padrão: português 'pt').
    """
    try:
        # Converte o texto em áudio
        tts = gTTS(text=texto, lang=idioma, slow=False)
        
        # Salva o áudio no formato MP3
        tts.save(arquivo_saida)
        
        # Reproduz o áudio gerado (no Windows, funciona diretamente)
        os.system(f"start {arquivo_saida}")  # Para Windows
        # os.system(f"mpg321 {arquivo_saida}")  # Para Linux (se mpg321 estiver instalado)
        # os.system(f"afplay {arquivo_saida}")  # Para macOS
        
        print(f"Áudio gerado e salvo como {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao converter texto em áudio: {e}")

def main():
    """
    Função principal para interagir com o usuário e gerar o áudio.
    """
    texto = input("Digite o texto que deseja converter em áudio: ")
    
    # Chama a função para converter texto em áudio
    texto_para_audio(texto)

if __name__ == "__main__":
    main()
