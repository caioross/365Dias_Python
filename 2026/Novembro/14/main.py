import PyPDF2

def extrair_metadados_pdf(caminho_arquivo):
    """
    Extrai metadados de um arquivo PDF.

    Args:
        caminho_arquivo (str): O caminho para o arquivo PDF.

    Returns:
        dict: Um dicionário contendo os metadados do PDF, incluindo autor, título, palavras-chave e software de criação.
    """
    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            leitor_pdf = PyPDF2.PdfFileReader(arquivo)
            metadados = leitor_pdf.getDocumentInfo()
            
            # Formata os metadados para uma saída mais legível
            metadados_formatados = {
                'Autor': metadados.get('/Author', 'Não disponível'),
                'Título': metadados.get('/Title', 'Não disponível'),
                'Palavras-chave': metadados.get('/Keywords', 'Não disponível'),
                'Software de criação': metadados.get('/Creator', 'Não disponível')
            }
            return metadados_formatados
    except Exception as e:
        print(f"Erro ao ler o arquivo PDF: {e}")
        return None

def main():
    """
    Função principal que executa o script.
    """
    caminho_arquivo = input("Digite o caminho para o arquivo PDF: ")
    metadados = extrair_metadados_pdf(caminho_arquivo)
    
    if metadados:
        print("\nMetadados do PDF:")
        for chave, valor in metadados.items():
            print(f"{chave}: {valor}")

if __name__ == '__main__':
    main()