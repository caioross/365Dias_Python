# 🐍 365 Dias de Python

![GitHub Repo Size](https://img.shields.io/github/repo-size/caioross/365dias_python?style=for-the-badge&color=blue)
![GitHub language count](https://img.shields.io/github/languages/count/caioross/365dias_python?style=for-the-badge&color=yellow)
![GitHub last commit](https://img.shields.io/github/last-commit/caioross/365dias_python?style=for-the-badge&color=green)
![License](https://img.shields.io/github/license/caioross/365dias_python?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![React](https://img.shields.io/badge/react-%2320232d.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)

> **O Desafio:** Criar, documentar e partilhar um script de Python diferente para cada dia do ano de 2026.

🌐 **Explora os scripts interativamente em:** [https://python365.vercel.app/](https://python365.vercel.app/)

---

## 🎯 Sobre o Projeto

Este repositório é um diário de aprendizagem contínua. O objetivo é explorar toda a versatilidade do Python — desde lógica básica e algoritmos até automação, análise de dados e integrações. 

Para tornar a experiência mais rica, os scripts não ficam apenas "escondidos" em pastas; desenvolvi uma **Single Page Application (SPA)** moderna que serve como um editor de código interativo para navegar por cada dia do desafio.

### Destaques do Site:
* **Interface Estilo IDE:** Visualização de código com syntax highlighting.
* **Terminal Integrado:** Simulação visual dos resultados dos scripts.
* **Documentação Dinâmica:** Renderização automática dos ficheiros `readme.md` de cada exercício.
* **Navegação Cronológica:** Filtro por meses e dias.

---

## 📂 Estrutura do Repositório

O projeto está dividido entre o **Núcleo de Scripts (Python)** e a **Plataforma Web (React)**.

```bash
365dias_python/
├── 2026/                 # 🐍 Scripts diários organizados cronologicamente
│   ├── Janeiro/
│   │   ├── 01/
│   │   │   ├── main.py   # Script do dia
│   │   │   └── readme.md # Explicação teórica/documentação
│   │   └── ...
│   └── ... (Todos os meses do ano)
├── src/                  # ⚛️ Código Fonte do Site (React + TypeScript)
│   ├── components/       # UI: Sidebar, EditorArea, TerminalArea, TopBar
│   ├── assets/           # Recursos estáticos (Logos, SVG)
│   ├── types.ts          # Definições de tipos TypeScript
│   └── App.tsx           # Lógica principal da aplicação
├── public/               # 📂 Arquivos Públicos e Base de Dados
│   ├── codes/            # Cópia dos scripts .py para carregamento no site
│   └── data.json         # O "Manifesto" que mapeia todos os dias e títulos
├── build-data.js         # 🛠️ Script de automação para gerar o data.json
├── package.json          # Dependências do ecossistema Node/React
└── vite.config.ts        # Configurações do ambiente de build (Vite)
```

## 🚀 Como Executar
## # 1. Executar Scripts Python Localmente
Navega até à pasta do dia específico e executa o ficheiro main.py:

```bash
python 2026/Janeiro/01/main.py
```

## #2. Executar o Site (Ambiente de Desenvolvimento)
Se quiseres rodar a interface web na tua máquina:
```bash
# Instalar dependências
npm install

# Iniciar o servidor de desenvolvimento
npm run dev
```

## 📝 Licença
Este projeto está licenciado sob a MIT License.


<div align="center">
<p>Desenvolvido com ❤️ por <a href="https://github.com/caioross">Caio Ross</a></p>
<a href="https://www.google.com/search?q=https://github.com/caioross/365dias_python">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Contribuir-Link%2520do%2520Repo-blueviolet%3Fstyle%3Dfor-the-badge%26logo%3Dgithub" alt="Link do Repositório">
</a>
</div>