"""
Script para gerar um arquivo HTML com o calendário do ano inteiro, permitindo a marcação de feriados.
"""

import calendar
from datetime import datetime

def generate_html_calendar(year, holidays):
    """
    Gera um calendário HTML para o ano especificado, marcando os feriados.

    :param year: Ano para o qual o calendário será gerado.
    :param holidays: Dicionário com as datas dos feriados no formato {'nome_do_feriado': 'DD-MM'}.
    :return: String contendo o código HTML do calendário.
    """
    html_calendar = f"<html><head><title>Calendário de {year}</title></head><body>"
    html_calendar += f"<h1>Calendário de {year}</h1>"

    for month in range(1, 13):
        html_calendar += f"<h2>{calendar.month_name[month]} {year}</h2>"
        html_calendar += "<table border='1'>"
        html_calendar += "<tr><th>Seg</th><th>Ter</th><th>Qua</th><th>Qui</th><th>Sex</th><th>Sáb</th><th>Dom</th></tr>"

        cal = calendar.monthcalendar(year, month)
        for week in cal:
            html_calendar += "<tr>"
            for day in week:
                if day == 0:
                    html_calendar += "<td></td>"
                else:
                    date_str = f"{day:02d}-{month:02d}"
                    if date_str in holidays:
                        html_calendar += f"<td style='background-color: yellow;'>{day}</td>"
                    else:
                        html_calendar += f"<td>{day}</td>"
            html_calendar += "</tr>"

        html_calendar += "</table>"

    html_calendar += "</body></html>"
    return html_calendar

def save_html_calendar(html_content, filename):
    """
    Salva o conteúdo HTML em um arquivo.

    :param html_content: String contendo o código HTML.
    :param filename: Nome do arquivo onde o HTML será salvo.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

def main():
    """
    Função principal que gera e salva o calendário HTML.
    """
    current_year = datetime.now().year
    holidays = {
        "Ano Novo": "01-01",
        "Dia da Independência": "04-09",
        "Natal": "25-12"
    }

    html_content = generate_html_calendar(current_year, holidays)
    save_html_calendar(html_content, "calendario.html")
    print(f"Calendário HTML salvo como 'calendario.html'.")

if __name__ == '__main__':
    main()