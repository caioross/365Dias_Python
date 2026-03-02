"""
Script para gerar um cardápio temático de Natal em formato PDF.
O cardápio inclui receitas com seus respectivos ingredientes.
"""

import os
from fpdf import FPDF

class CardapioNatalinoPDF(FPDF):
    """
    Classe para criar um PDF de cardápio natalino.
    """
    def header(self):
        """
        Adiciona o cabeçalho ao PDF.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Cardápio Natalino', 0, 1, 'C')

    def footer(self):
        """
        Adiciona o rodapé ao PDF.
        """
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def add_receita(self, nome, ingredientes):
        """
        Adiciona uma receita ao PDF.

        :param nome: Nome da receita.
        :param ingredientes: Lista de ingredientes da receita.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, nome, 0, 1)
        self.set_font('Arial', '', 10)
        for ingrediente in ingredientes:
            self.cell(0, 10, f'- {ingrediente}', 0, 1)

def main():
    """
    Função principal para criar o PDF do cardápio natalino.
    """
    pdf = CardapioNatalinoPDF()
    pdf.add_page()

    receitas = [
        {
            'nome': 'Torta de Maçã',
            'ingredientes': [
                '2 maçãs',
                '1 xícara de açúcar',
                '1/2 xícara de farinha de trigo',
                '1 colher de sopa de fermento em pó',
                '1 colher de sopa de manteiga derretida'
            ]
        },
        {
            'nome': 'Pão de Noz',
            'ingredientes': [
                '2 xícaras de farinha de trigo',
                '1 xícara de nozes picadas',
                '1 colher de chá de fermento em pó',
                '1/2 colher de chá de sal',
                '1/2 xícara de leite',
                '3 ovos',
                '1 colher de sopa de óleo'
            ]
        },
        {
            'nome': 'Bolo de Chocolate',
            'ingredientes': [
                '2 xícaras de farinha de trigo',
                '1 xícara de cacau em pó',
                '1/2 xícara de açúcar',
                '1/2 xícara de óleo',
                '2 ovos',
                '1 xícara de leite',
                '1 colher de sopa de fermento em pó',
                '1 colher de chá de bicarbonato de sódio',
                '1/2 colher de chá de sal'
            ]
        }
    ]

    for receita in receitas:
        pdf.add_receita(receita['nome'], receita['ingredientes'])

    pdf.output('cardapio_natalino.pdf')

if __name__ == '__main__':
    main()