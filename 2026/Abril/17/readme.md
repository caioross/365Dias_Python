# 📄 Leitor PDF Páginas Específicas

Este script extrai o texto de um intervalo de páginas selecionado pelo usuário em um arquivo PDF, facilitando a extração de informações específicas de documentos longos.

## ✨ Funcionalidades
- Permite ao usuário selecionar um intervalo de páginas para extração.
- Extrai o texto das páginas especificadas.
- Saída do texto extraído no terminal ou em um arquivo de texto.

## 🛠️ Pré-requisitos
- Python 3.x instalado na sua máquina.
- Biblioteca externa `PyPDF2` necessária para manipulação de PDFs. Pode ser instalada via pip:

```bash
pip install PyPDF2
```

## 🚀 Como Executar

1. Navegue até à pasta do script no seu terminal.
2. Execute o comando abaixo, substituindo `nome_do_arquivo.pdf` pelo nome do seu arquivo PDF e `1 3` pelo intervalo de páginas desejado:

```bash
python leitor_pdf_paginas_especificas.py nome_do_arquivo.pdf 1 3
```

## 365 Dias de Python
Este projeto faz parte do desafio 365 Dias de Python, um compromisso de programar e publicar um novo script útil todos os dias durante o ano de 2026.

---

Este README.md foi criado seguindo as diretrizes fornecidas para garantir que o script seja facilmente compreendido e executado por qualquer pessoa interessada.