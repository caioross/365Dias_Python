"""
Script para gerar um recibo de pagamento em PDF com assinatura digital.
"""

import os
from fpdf import FPDF
from cryptography.fernet import Fernet

class PDFRecibo(FPDF):
    """
    Classe para criar um PDF de recibo de pagamento.
    """
    def header(self):
        """
        Cabeçalho do PDF.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Recibo de Pagamento', 0, 1, 'C')

    def footer(self):
        """
        Rodapé do PDF.
        """
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def add_recibo_details(self, cliente, servico, valor):
        """
        Adiciona os detalhes do recibo ao PDF.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'Cliente: {cliente}', 0, 1)
        self.cell(0, 10, f'Serviço: {servico}', 0, 1)
        self.cell(0, 10, f'Valor: R$ {valor:.2f}', 0, 1)

def gerar_pdf_recibo(cliente, servico, valor, output_path):
    """
    Gera um PDF de recibo com os detalhes fornecidos.
    """
    pdf = PDFRecibo()
    pdf.add_page()
    pdf.add_recibo_details(cliente, servico, valor)
    pdf.output(output_path)

def assinar_pdf(input_path, output_path, key):
    """
    Assina digitalmente um PDF usando uma chave de criptografia.
    """
    with open(input_path, 'rb') as file:
        pdf_data = file.read()
    
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(pdf_data)
    
    with open(output_path, 'wb') as file:
        file.write(encrypted_data)

def main():
    """
    Função principal para gerar e assinar o recibo.
    """
    cliente = "João Silva"
    servico = "Desenvolvimento de Software"
    valor = 3000.00
    output_path = "recibo.pdf"
    signed_output_path = "recibo_assinado.pdf"
    
    # Gerar o PDF do recibo
    gerar_pdf_recibo(cliente, servico, valor, output_path)
    
    # Gerar uma chave de criptografia
    key = Fernet.generate_key()
    
    # Assinar o PDF
    assinar_pdf(output_path, signed_output_path, key)
    
    print(f"Recibo gerado e assinado em: {signed_output_path}")

if __name__ == '__main__':
    main()