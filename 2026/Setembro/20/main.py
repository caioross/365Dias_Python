"""
validador_seguranca_ssh.py

Script para analisar o arquivo de configuração do SSH e sugerir melhorias de segurança.
"""

import os
import sys

def analisar_ssh_config(arquivo_config):
    """
    Analisa o arquivo de configuração do SSH e sugere melhorias de segurança.

    :param arquivo_config: Caminho para o arquivo de configuração do SSH.
    :return: Lista de sugestões de melhorias.
    """
    if not os.path.exists(arquivo_config):
        raise FileNotFoundError(f"O arquivo de configuração {arquivo_config} não foi encontrado.")

    sugestoes = []
    with open(arquivo_config, 'r') as file:
        for linha in file:
            linha = linha.strip()
            if linha.startswith('#') or not linha:
                continue

            if 'PermitRootLogin' in linha and 'yes' in linha:
                sugestoes.append("Desative o login root. Use 'PermitRootLogin no'.")

            if 'PasswordAuthentication' in linha and 'yes' in linha:
                sugestoes.append("Desative a autenticação por senha. Use 'PasswordAuthentication no'.")

            if 'UsePAM' not in linha:
                sugestoes.append("Considere usar PAM para autenticação. Adicione 'UsePAM yes'.")

            if 'AllowUsers' not in linha and 'AllowGroups' not in linha:
                sugestoes.append("Restrinja o acesso a usuários específicos usando 'AllowUsers' ou 'AllowGroups'.")

    return sugestoes

def main():
    """
    Função principal do script.
    """
    if len(sys.argv) != 2:
        print("Uso: python validador_seguranca_ssh.py <caminho_do_arquivo_ssh_config>")
        sys.exit(1)

    arquivo_config = sys.argv[1]
    try:
        sugestoes = analisar_ssh_config(arquivo_config)
        if sugestoes:
            print("Sugestões para melhorar a segurança do SSH:")
            for sugestao in sugestoes:
                print(f"- {sugestao}")
        else:
            print("O arquivo de configuração SSH parece estar seguro.")
    except Exception as e:
        print(f"Erro ao analisar o arquivo de configuração SSH: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()