import requests

def is_cnpj_active(cnpj):
    """
    Verifica se o CNPJ está ativo na base da Receita Federal.

    Args:
        cnpj (str): CNPJ a ser verificado. Deve ser uma string de 14 dígitos.

    Returns:
        bool: True se o CNPJ estiver ativo, False caso contrário.
    """
    if len(cnpj) != 14 or not cnpj.isdigit():
        raise ValueError("CNPJ deve ser uma string de 14 dígitos numéricos.")

    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('status', '').lower() == 'ativa'
    else:
        raise Exception(f"Erro ao consultar CNPJ: {response.status_code} - {response.text}")

def main():
    """
    Função principal que solicita um CNPJ ao usuário e verifica se ele está ativo.
    """
    cnpj = input("Digite o CNPJ (14 dígitos): ")
    try:
        if is_cnpj_active(cnpj):
            print("O CNPJ está ativo.")
        else:
            print("O CNPJ não está ativo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()