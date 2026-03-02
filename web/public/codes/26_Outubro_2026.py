"""
Script para gerar um relatório executivo em PDF a partir de logs de um mês.
"""

import os
from datetime import datetime
from fpdf import FPDF

def agrupa_logs_por_data(logs):
    """
    Agrupa logs por data.

    Args:
        logs (list): Lista de logs, onde cada log é uma string.

    Returns:
        dict: Um dicionário onde as chaves são datas e os valores são listas de logs para cada data.
    """
    logs_agrupados = {}
    for log in logs:
        data = log.split()[0]  # Assuming the date is the first element in the log string
        if data not in logs_agrupados:
            logs_agrupados[data] = []
        logs_agrupados[data].append(log)
    return logs_agrupados

def cria_pdf(logs_agrupados, nome_arquivo):
    """
    Cria um PDF com os logs agrupados por data.

    Args:
        logs_agrupados (dict): Dicionário com logs agrupados por data.
        nome_arquivo (str): Nome do arquivo PDF a ser gerado.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for data, logs in logs_agrupados.items():
        pdf.cell(200, 10, txt=f"Data: {data}", ln=True, align='C')
        for log in logs:
            pdf.cell(200, 10, txt=log, ln=True)
        pdf.ln(10)  # Adiciona uma linha em branco entre os dias

    pdf.output(nome_arquivo)

def main():
    """
    Função principal para gerar o relatório PDF a partir dos logs.
    """
    # Exemplo de logs, em um cenário real, isso poderia ser lido de um arquivo ou banco de dados
    logs = [
        "2023-10-01 08:00:00 Log 1",
        "2023-10-01 09:00:00 Log 2",
        "2023-10-02 10:00:00 Log 3",
        "2023-10-02 11:00:00 Log 4",
    ]

    logs_agrupados = agrupa_logs_por_data(logs)
    nome_arquivo = f"relatorio_mensal_{datetime.now().strftime('%Y-%m')}.pdf"
    cria_pdf(logs_agrupados, nome_arquivo)
    print(f"Relatório gerado com sucesso: {nome_arquivo}")

if __name__ == '__main__':
    main()