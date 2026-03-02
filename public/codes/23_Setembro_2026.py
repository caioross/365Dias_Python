"""
Script para gerar etiquetas de remetente e destinatário no padrão oficial dos Correios.
"""

import os
from fpdf import FPDF

class PDF(FPDF):
    """
    Classe PDF personalizada para gerar etiquetas de correios.
    """
    def header(self):
        """
        Adiciona o cabeçalho da etiqueta.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'ETIQUETA DE CORREIOS', 0, 1, 'C')

    def footer(self):
        """
        Adiciona o rodapé da etiqueta.
        """
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def add_address(self, address):
        """
        Adiciona um endereço à etiqueta.
        :param address: Dicionário contendo os detalhes do endereço.
        """
        self.set_font('Arial', '', 10)
        for key, value in address.items():
            self.cell(0, 10, f'{key}: {value}', 0, 1)

def main():
    """
    Função principal para gerar o PDF de etiquetas.
    """
    # Exemplo de endereços
    addresses = [
        {
            'Nome': 'João Silva',
            'Endereço': 'Rua das Flores, 123',
            'Bairro': 'Centro',
            'CEP': '12345-678',
            'Cidade': 'São Paulo',
            'UF': 'SP'
        },
        {
            'Nome': 'Maria Oliveira',
            'Endereço': 'Avenida dos Sonhos, 456',
            'Bairro': 'Jardins',
            'CEP': '87654-321',
            'Cidade': 'Rio de Janeiro',
            'UF': 'RJ'
        }
    ]

    pdf = PDF()
    pdf.add_page()

    for address in addresses:
        pdf.add_address(address)
        pdf.add_page()  # Nova página para o próximo endereço

    output_path = 'etiquetas_correios.pdf'
    pdf.output(output_path)
    print(f'PDF gerado com sucesso em: {os.path.abspath(output_path)}')

if __name__ == '__main__':
    main()