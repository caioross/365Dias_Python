"""
gerador_termos_uso_site.py

Script para gerar um rascunho de termos de uso e política de privacidade para sites.
"""

def gerar_termos_de_uso():
    """
    Gera um rascunho básico de termos de uso para um site.
    """
    termos_de_uso = """
    Termos de Uso

    Bem-vindo ao [Nome do Site]. Estes Termos de Uso descrevem as regras e regulamentos para o uso deste site [Nome do Site], localizado em [URL do Site].

    Uso Aceitável
    1. Você não pode usar o site para qualquer finalidade ilegal ou antiética.
    2. Você não pode violar a privacidade de outros usuários ou coletar informações pessoais sem o consentimento explícito.

    Propriedade Intelectual
    1. Todo o conteúdo do site, incluindo textos, imagens, logotipos e design, é de propriedade do [Nome da Empresa] ou de seus licenciadores e está protegido por leis de direitos autorais.

    Limitação de Responsabilidade
    1. Em nenhuma circunstância o [Nome da Empresa] será responsável por qualquer perda ou dano, direto ou indireto, decorrente do uso ou incapacidade de usar este site.

    Modificações
    1. Estes Termos de Uso podem ser modificados a qualquer momento sem aviso prévio. É sua responsabilidade revisar regularmente estes Termos de Uso.

    Aceitação
    1. Ao usar este site, você concorda com estes Termos de Uso e com nossa Política de Privacidade.

    Contato
    1. Para quaisquer perguntas sobre estes Termos de Uso, entre em contato conosco em [Email de Contato].

    [Data]
    """
    return termos_de_uso

def gerar_politica_de_privacidade():
    """
    Gera um rascunho básico de política de privacidade para um site.
    """
    politica_de_privacidade = """
    Política de Privacidade

    A privacidade dos nossos usuários é extremamente importante para nós. Esta Política de Privacidade explica como coletamos, usamos, divulgamos e protegemos suas informações pessoais ao usar o site [Nome do Site], localizado em [URL do Site].

    Coleta de Informações
    1. Coletamos informações pessoais que você fornece voluntariamente, como seu nome, endereço de e-mail e informações de contato.

    Uso de Informações
    1. Utilizamos suas informações para fornecer e melhorar nossos serviços, responder a suas solicitações e para fins de comunicação.

    Proteção de Informações
    1. Implementamos medidas de segurança para proteger suas informações pessoais contra acesso não autorizado, alteração, divulgação ou destruição.

    Cookies
    1. Usamos cookies para melhorar a experiência do usuário. Os cookies são pequenos arquivos de dados que são armazenados no seu navegador.

    Consentimento
    1. Ao usar este site, você concorda com nossa coleta, uso e divulgação de suas informações pessoais conforme descrito nesta Política de Privacidade.

    Modificações
    1. Esta Política de Privacidade pode ser modificada a qualquer momento sem aviso prévio. É sua responsabilidade revisar regularmente esta Política de Privacidade.

    Contato
    1. Para quaisquer perguntas sobre esta Política de Privacidade, entre em contato conosco em [Email de Contato].

    [Data]
    """
    return politica_de_privacidade

def main():
    """
    Função principal que gera e imprime os termos de uso e a política de privacidade.
    """
    print("Rascunho de Termos de Uso:")
    print(gerar_termos_de_uso())
    print("\nRascunho de Política de Privacidade:")
    print(gerar_politica_de_privacidade())

if __name__ == '__main__':
    main()