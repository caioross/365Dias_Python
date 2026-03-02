import csv
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Cardápio do Restaurante', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def gerar_pdf(pratos, precos, nome_pdf):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for prato, preco in zip(pratos, precos):
        pdf.cell(0, 10, f'{prato}: R${preco:.2f}', 0, 1)

    pdf.output(nome_pdf)

def ler_csv(caminho_csv):
    pratos = []
    precos = []
    with open(caminho_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pula a linha de cabeçalho
        for row in reader:
            pratos.append(row[0])
            precos.append(float(row[1]))
    return pratos, precos

def main():
    caminho_csv = 'menu.csv'
    nome_pdf = 'cardapio.pdf'
    
    pratos, precos = ler_csv(caminho_csv)
    gerar_pdf(pratos, precos, nome_pdf)
    print(f'Cardápio gerado com sucesso como {nome_pdf}')

if __name__ == '__main__':
    main()