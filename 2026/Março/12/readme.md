# 📡 Gerador de QR Code para Conexão Wi-Fi

Este script Python gera um QR Code que permite a conexão automática a uma rede Wi-Fi ao ser escaneado, simplificando o processo de configuração de redes.

## ✨ Funcionalidades
- Geração de um QR Code que inclui informações de conexão Wi-Fi.
- Suporte para redes Wi-Fi protegidas (WPA/WPA2).
- Saída do QR Code em formato de imagem (PNG).

## 🛠️ Pré-requisitos
- Python 3.x instalado na sua máquina.
- Biblioteca externa `qrcode` para geração do QR Code.
- Biblioteca externa `Pillow` para manipulação de imagens.

Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:

```bash
pip install qrcode[pil]
```

## 🚀 Como Executar

1. Navegue até à pasta do script no seu terminal.
2. Execute o comando abaixo:

```bash
python gerador_qr_code_wifi.py
```

3. Siga as instruções no terminal para inserir o nome da rede Wi-Fi e a senha (se necessário).

## 365 Dias de Python
Este projeto faz parte do desafio 365 Dias de Python, um compromisso de programar e publicar um novo script útil todos os dias durante o ano de 2026.

---

Este README.md foi criado seguindo as diretrizes fornecidas, garantindo que o script seja fácil de entender e executar, enquanto mantém a aparência profissional e a narrativa do desafio 365 Dias de Python.