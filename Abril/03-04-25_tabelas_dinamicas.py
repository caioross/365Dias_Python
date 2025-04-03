from flask import Flask, render_template_string

app = Flask(__name__)

# Lista de dados para criar a tabela
dados = [
    {"nome": "João", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Pedro", "idade": 28, "cidade": "Belo Horizonte"}
]

# Rota principal que renderiza a página com a tabela
@app.route('/')
def exibir_tabela():
    # HTML com a estrutura da tabela
    tabela_html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabela de Dados</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 8px 12px;
                border: 1px solid #ddd;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>Tabela de Pessoas</h2>
        <table>
            <tr>
                <th>Nome</th>
                <th>Idade</th>
                <th>Cidade</th>
            </tr>
            {% for pessoa in dados %}
            <tr>
                <td>{{ pessoa.nome }}</td>
                <td>{{ pessoa.idade }}</td>
                <td>{{ pessoa.cidade }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    # Renderiza o template HTML com os dados
    return render_template_string(tabela_html, dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
