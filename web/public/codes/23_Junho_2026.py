import os
from fpdf import FPDF
from datetime import datetime

class Fatura:
    """
    Classe para representar uma fatura profissional.
    
    Atributos:
    - cliente: Nome do cliente.
    - itens: Lista de itens da fatura, onde cada item é um dicionário com 'descricao', 'quantidade' e 'preco_unitario'.
    - taxa_imposto: Taxa de imposto a ser aplicada sobre o subtotal.
    """
    
    def __init__(self, cliente, itens, taxa_imposto=0.18):
        self.cliente = cliente
        self.itens = itens
        self.taxa_imposto = taxa_imposto

    def calcular_subtotal(self):
        """
        Calcula o subtotal da fatura.
        
        Retorna:
        - Subtotal calculado.
        """
        return sum(item['quantidade'] * item['preco_unitario'] for item in self.itens)

    def calcular_imposto(self):
        """
        Calcula o valor do imposto.
        
        Retorna:
        - Valor do imposto.
        """
        subtotal = self.calcular_subtotal()
        return subtotal * self.taxa_imposto

    def calcular_total(self):
        """
        Calcula o total da fatura, incluindo imposto.
        
        Retorna:
        - Total calculado.
        """
        subtotal = self.calcular_subtotal()
        imposto = self.calcular_imposto()
        return subtotal + imposto

    def gerar_pdf(self, nome_arquivo):
        """
        Gera um PDF da fatura.
        
        Parâmetros:
        - nome_arquivo: Nome do arquivo PDF a ser gerado.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Fatura", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Cliente: {self.cliente}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Data: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align='L')
        pdf.cell(200, 10, txt="Itens:", ln=True, align='L')

        for item in self.itens:
            pdf.cell(200, 10, txt=f"{item['descricao']} - {item['quantidade']} x {item['preco_unitario']:.2f} = {item['quantidade'] * item['preco_unitario']:.2f}", ln=True, align='L')

        pdf.cell(200, 10, txt=f"Subtotal: {self.calcular_subtotal():.2f}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Imposto ({self.taxa_imposto * 100}%): {self.calcular_imposto():.2f}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Total: {self.calcular_total():.2f}", ln=True, align='L')

        pdf.output(nome_arquivo)

def main():
    itens = [
        {'descricao': 'Serviço de Consultoria', 'quantidade': 2, 'preco_unitario': 500.00},
        {'descricao': 'Desenvolvimento de Software', 'quantidade': 1, 'preco_unitario': 1500.00}
    ]
    fatura = Fatura(cliente="João da Silva", itens=itens)
    fatura.gerar_pdf("fatura.pdf")
    print("Fatura gerada com sucesso!")

if __name__ == '__main__':
    main()