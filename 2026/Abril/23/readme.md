# 📊 Extrair Tabelas Site

Este script captura todas as tabelas HTML de uma URL fornecida e as converte em arquivos CSV individuais, facilitando a análise e o processamento de dados estruturados.

## ✨ Funcionalidades
- Captura todas as tabelas HTML de uma página web.
- Converte cada tabela em um arquivo CSV separado.
- Nomeia os arquivos CSV de acordo com o título da tabela ou um índice sequencial.
- Suporta URLs com múltiplas tabelas.

## 🛠️ Pré-requisitos
- Python 3.x instalado na sua máquina.
- Bibliotecas externas necessárias:
  - `requests` para fazer requisições HTTP.
  - `pandas` para manipulação e exportação de dados em formato CSV.

## 🚀 Como Executar

1. Navegue até à pasta do script no seu terminal.
2. Execute o comando abaixo, substituindo `URL_DO_SITE` pela URL do site que deseja extrair as tabelas:

```bash
python extrair_tabelas_site.py URL_DO_SITE
```

## 365 Dias de Python
Este projeto faz parte do desafio 365 Dias de Python, um compromisso de programar e publicar um novo script útil todos os dias durante o ano de 2026.

---

Este README.md foi criado seguindo as diretrizes fornecidas, garantindo que o script seja fácil de entender e executar, enquanto mantém a integridade do projeto "365 Dias de Python".