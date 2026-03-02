"""
gerador_mensagem_gratidao.py

Este script gera mensagens personalizadas de agradecimento de fim de ano para clientes e amigos.
"""

def gerar_mensagem_personalizada(nome: str, tipo: str) -> str:
    """
    Gera uma mensagem de agradecimento personalizada.

    Args:
        nome (str): O nome da pessoa para quem a mensagem é direcionada.
        tipo (str): O tipo de mensagem ('cliente' ou 'amigo').

    Returns:
        str: A mensagem de agradecimento personalizada.
    """
    if tipo == 'cliente':
        return f"Querido(a) {nome},\n\nAgradecemos por sua fidelidade ao nosso negócio este ano. Que o próximo ano seja ainda mais produtivo e repleto de sucesso!\n\nAtenciosamente,\nSeu time de suporte."
    elif tipo == 'amigo':
        return f"Querido(a) {nome},\n\nDesejo um Feliz Ano Novo repleto de saúde, amor e realizações. Que nossas amizades se fortaleçam ainda mais no próximo ano!\n\nCom carinho,\n[Seu Nome]"
    else:
        raise ValueError("Tipo de mensagem inválido. Use 'cliente' ou 'amigo'.")

def main():
    """
    Função principal que gera e imprime mensagens de agradecimento.
    """
    clientes = ["João", "Maria", "Carlos"]
    amigos = ["Ana", "Pedro", "Juliana"]

    print("Mensagens para clientes:")
    for cliente in clientes:
        print(gerar_mensagem_personalizada(cliente, 'cliente'))
        print("\n" + "-"*40 + "\n")

    print("Mensagens para amigos:")
    for amigo in amigos:
        print(gerar_mensagem_personalizada(amigo, 'amigo'))
        print("\n" + "-"*40 + "\n")

if __name__ == '__main__':
    main()