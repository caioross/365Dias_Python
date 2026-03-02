# 🔗 Verificador de Links Quebrados

Este script escaneia um site e identifica links que retornam erro 404 (não encontrado), ajudando a manter a integridade e a qualidade do conteúdo web.

## ✨ Funcionalidades
- **Análise de Links:** Verifica todos os links em uma página web específica.
- **Detecção de Erros 404:** Identifica links que retornam erro 404, indicando que a página solicitada não foi encontrada.
- **Relatório de Links Quebrados:** Gera um relatório com a lista de links quebrados.

## 🛠️ Pré-requisitos
- **Python 3.x** instalado na sua máquina.
- **Bibliotecas Externas:** O script utiliza a biblioteca `requests` para fazer requisições HTTP. Para instalá-la, execute o comando abaixo:
  ```bash
  pip install requests
  ```

## 🚀 Como Executar

1. Navegue até à pasta do script no seu terminal.
2. Execute o comando abaixo, substituindo `URL_DO_SITE` pelo endereço do site que deseja analisar:

```bash
python main.py URL_DO_SITE
```

## 365 Dias de Python
Este projeto faz parte do desafio 365 Dias de Python, um compromisso de programar e publicar um novo script útil todos os dias durante o ano de 2026.