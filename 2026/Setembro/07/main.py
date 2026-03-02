"""
gerador_template_flask.py

Script para criar automaticamente a estrutura de pastas e arquivos base para um novo projeto Web Flask.
"""

import os

def create_directory(path):
    """Cria um diretório se ele não existir."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Criado diretório: {path}")

def create_file(path, content=""):
    """Cria um arquivo com o conteúdo fornecido."""
    with open(path, 'w') as file:
        file.write(content)
        print(f"Criado arquivo: {path}")

def generate_flask_project(project_name):
    """Gera a estrutura básica de um projeto Flask."""
    # Estrutura básica de pastas
    project_path = os.path.join(os.getcwd(), project_name)
    create_directory(project_path)
    create_directory(os.path.join(project_path, 'templates'))
    create_directory(os.path.join(project_path, 'static'))
    create_directory(os.path.join(project_path, 'static', 'css'))
    create_directory(os.path.join(project_path, 'static', 'js'))
    create_directory(os.path.join(project_path, 'static', 'images'))
    create_directory(os.path.join(project_path, 'app'))
    create_directory(os.path.join(project_path, 'app', 'templates'))

    # Arquivo principal do projeto
    app_py_content = """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
"""
    create_file(os.path.join(project_path, 'app.py'), app_py_content)

    # Arquivo de configuração
    config_py_content = """class Config:
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
"""
    create_file(os.path.join(project_path, 'app', 'config.py'), config_py_content)

    # Arquivo de rotas
    routes_py_content = """from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Hello, Flask!'
"""
    create_file(os.path.join(project_path, 'app', 'routes.py'), routes_py_content)

    # Arquivo HTML base
    index_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>Bem-vindo ao Flask!</h1>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
"""
    create_file(os.path.join(project_path, 'templates', 'index.html'), index_html_content)

    # Arquivo CSS base
    style_css_content = """body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

h1 {
    color: #333;
}
"""
    create_file(os.path.join(project_path, 'static', 'css', 'style.css'), style_css_content)

    # Arquivo JavaScript base
    script_js_content = """console.log("Flask app is running!");
"""
    create_file(os.path.join(project_path, 'static', 'js', 'script.js'), script_js_content)

    print(f"Projeto Flask '{project_name}' criado com sucesso!")

def main():
    project_name = input("Digite o nome do projeto Flask: ")
    generate_flask_project(project_name)

if __name__ == '__main__':
    main()