import PyPDF2

def ler_pdf(caminho_pdf):
    """
    Função para ler e extrair texto de um arquivo PDF.
    
    :param caminho_pdf: Caminho do arquivo PDF a ser lido.
    :return: Texto extraído do PDF.
    """
    try:
        # Abre o arquivo PDF
        with open(caminho_pdf, "rb") as file:
            # Cria um objeto PDF reader
            pdf_reader = PyPDF2.PdfReader(file)

            # Extrai texto de todas as páginas
            texto = ""
            for page_num in range(len(pdf_reader.pages)):
                pagina = pdf_reader.pages[page_num]
                texto += pagina.extract_text()

            return texto
    except Exception as e:
        print(f"Erro ao ler o arquivo PDF: {e}")
        return None

def escrever_pdf(caminho_saida, texto):
    """
    Função para escrever texto em um arquivo PDF.
    
    :param caminho_saida: Caminho do arquivo PDF de saída.
    :param texto: Texto a ser escrito no PDF.
    """
    try:
        # Cria um objeto PDF writer
        pdf_writer = PyPDF2.PdfWriter()

        # Cria uma página em branco
        pagina = PyPDF2.pdf.PageObject.createBlankPage(None, 612, 792)

        # Adiciona o texto na página em branco (não é uma solução ideal para texto no PDF)
        pagina.insertText(texto)

        # Adiciona a página ao PDF writer
        pdf_writer.add_page(pagina)

        # Cria o arquivo de saída
        with open(caminho_saida, "wb") as output_pdf:
            pdf_writer.write(output_pdf)

        print(f"PDF escrito com sucesso em: {caminho_saida}")
    except Exception as e:
        print(f"Erro ao escrever o arquivo PDF: {e}")

def main():
    """
    Função principal para ler e escrever arquivos PDF.
    """
    # Escolher o arquivo de entrada e saída
    caminho_pdf = input("Digite o caminho do arquivo PDF para ler: ")
    caminho_saida = input("Digite o caminho do arquivo PDF de saída: ")

    # Lê o conteúdo do PDF
    texto_extraido = ler_pdf(caminho_pdf)
    if texto_extraido:
        print("Texto extraído do PDF:")
        print(texto_extraido)

        # Escreve o texto extraído em um novo PDF
        escrever_pdf(caminho_saida, texto_extraido)

if __name__ == "__main__":
    main()
