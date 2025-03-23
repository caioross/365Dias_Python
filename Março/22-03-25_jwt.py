import jwt
import datetime

# Chave secreta para assinatura do token (mantenha isso seguro)
SECRET_KEY = "minha_chave_secreta"

# Usuários "fictícios" para autenticação (em um caso real, viria de um banco de dados)
USUARIOS = {
    "usuario1": "senha1",
    "usuario2": "senha2"
}

def gerar_token(usuario):
    """
    Função para gerar um JWT (token) para o usuário.
    :param usuario: nome do usuário
    :return: token JWT
    """
    # Define o tempo de expiração (1 hora)
    expirar_em = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    # Gera o token JWT
    token = jwt.encode(
        {"username": usuario, "exp": expirar_em}, SECRET_KEY, algorithm="HS256"
    )
    return token

def verificar_token(token):
    """
    Função para verificar a validade do token JWT.
    :param token: token JWT para verificação
    :return: dados do usuário se o token for válido, ou erro
    """
    try:
        # Decodifica e valida o token
        dados = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return dados
    except jwt.ExpiredSignatureError:
        # Token expirado
        return "O token expirou. Faça login novamente."
    except jwt.InvalidTokenError:
        # Token inválido
        return "Token inválido."

def login(usuario, senha):
    """
    Função de login para gerar o token JWT se as credenciais forem corretas.
    :param usuario: nome do usuário
    :param senha: senha fornecida
    :return: token JWT ou erro
    """
    if usuario in USUARIOS and USUARIOS[usuario] == senha:
        # Gera o token para o usuário
        token = gerar_token(usuario)
        return f"Login bem-sucedido! Seu token é: {token}"
    else:
        return "Credenciais inválidas."

def main():
    """
    Função principal para interagir com o usuário.
    """
    while True:
        print("\nAutenticação com JWT")
        print("1. Login")
        print("2. Verificar Token")
        print("3. Sair")

        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == "1":
            # Realiza o login
            usuario = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            resultado = login(usuario, senha)
            print(resultado)

        elif opcao == "2":
            # Verifica o token
            token = input("Digite o seu token JWT: ")
            resultado = verificar_token(token)
            print(resultado)

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
