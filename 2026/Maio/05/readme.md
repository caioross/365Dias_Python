# 📸 Organizador de Fotos Camera

Este script organiza fotos baseando-se no modelo da câmera extraído dos metadados EXIF, facilitando a gestão e a classificação de imagens.

## ✨ Funcionalidades
- **Extração de Metadados EXIF:** Recupera informações detalhadas sobre a câmera usada para tirar a foto.
- **Organização Automática:** Move as fotos para pastas nomeadas de acordo com o modelo da câmera.
- **Relatório de Processamento:** Gera um log com detalhes sobre o processamento de cada imagem.

## 🛠️ Pré-requisitos
- Python 3.x instalado na sua máquina.
- Biblioteca `Pillow` para manipulação de imagens.
- Biblioteca `piexif` para extração de metadados EXIF.

Para instalar as bibliotecas necessárias, execute:

```bash
pip install Pillow piexif
```

## 🚀 Como Executar

1. Navegue até à pasta do script no seu terminal.
2. Execute o comando abaixo:

```bash
python organizador_fotos_camera.py
```

## 365 Dias de Python
Este projeto faz parte do desafio 365 Dias de Python, um compromisso de programar e publicar um novo script útil todos os dias durante o ano de 2026.