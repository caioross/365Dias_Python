import requests

def buscar_endereco_por_cep(cep):
    """
    Busca o endereço completo (Rua, Bairro, Cidade) a partir de um CEP informado.

    Args:
        cep (str): O CEP a ser consultado.

    Returns:
        dict: Um dicionário contendo as informações do endereço ou None se o CEP não for encontrado.
    """
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return {
                'rua': data.get('logradouro'),
                'bairro': data.get('bairro'),
                'cidade': data.get('localidade')
            }
    return None

def main():
    """
    Função principal que solicita um CEP ao usuário e exibe o endereço correspondente.
    """
    cep = input("Digite o CEP (apenas números): ")
    endereco = buscar_endereco_por_cep(cep)
    
    if endereco:
        print(f"Endereço para o CEP {cep}:")
        print(f"Rua: {endereco['rua']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['cidade']}")
    else:
        print("CEP não encontrado ou inválido.")

if __name__ == '__main__':
    main()