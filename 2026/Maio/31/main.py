"""
Script para gerar certificados de participação em massa a partir de uma lista de nomes.
"""

import os
from fpdf import FPDF

class PDF(FPDF):
    """
    Classe PDF personalizada para criar certificados.
    """
    def header(self):
        """
        Adiciona o cabeçalho ao certificado.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Certificado de Participação', 0, 1, 'C')

    def footer(self):
        """
        Adiciona o rodapé ao certificado.
        """
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def gerar_certificado(pdf, nome):
    """
    Gera um certificado para um nome específico.

    :param pdf: Instância da classe PDF.
    :param nome: Nome do participante.
    """
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 100, f'Certificamos que {nome} participou do evento.', 0, 1, 'C')

def main():
    """
    Função principal para gerar certificados em massa.
    """
    nomes_participantes = [
        'João Silva',
        'Maria Oliveira',
        'Carlos Pereira',
        'Ana Costa'
    ]

    pdf = PDF()
    for nome in nomes_participantes:
        gerar_certificado(pdf, nome)

    # Salva o PDF com os certificados
    pdf.output('certificados.pdf')
    print('Certificados gerados com sucesso!')

if __name__ == '__main__':
    main()