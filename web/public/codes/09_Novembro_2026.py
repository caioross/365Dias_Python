import math

def calcular_probabilidade_condicional(prior, likelihood, evidence):
    """
    Calcula a probabilidade condicional usando o Teorema de Bayes.

    Args:
    prior (float): A probabilidade a priori da hipótese.
    likelihood (float): A probabilidade do dado dado a hipótese.
    evidence (float): A probabilidade do dado.

    Returns:
    float: A probabilidade a posteriori da hipótese.
    """
    return (prior * likelihood) / evidence

def calcular_evidencia(probabilidades_hipoteses, likelihoods):
    """
    Calcula a probabilidade do dado (evidência) usando as probabilidades das hipóteses e likelihoods.

    Args:
    probabilidades_hipoteses (list of float): As probabilidades a priori das hipóteses.
    likelihoods (list of float): As probabilidades do dado dado cada hipótese.

    Returns:
    float: A probabilidade do dado.
    """
    evidence = 0
    for prior, likelihood in zip(probabilidades_hipoteses, likelihoods):
        evidence += prior * likelihood
    return evidence

def main():
    """
    Função principal que demonstra o uso do Teorema de Bayes.
    """
    # Exemplo: Teste de uma moeda
    # Hipóteses: H0 (moeda justa) e H1 (moeda viciada)
    hipoteses = ['H0', 'H1']
    probabilidades_hipoteses = [0.5, 0.5]  # Probabilidades a priori igualmente prováveis
    resultados = ['Cara', 'Cara']  # Resultados observados

    # Likelihoods para cada hipótese e resultado
    likelihoods = {
        'H0': [0.5, 0.5],  # Probabilidade de cara ou coroa para uma moeda justa
        'H1': [0.9, 0.1]   # Probabilidade de cara para uma moeda viciada
    }

    # Calcular a evidência
    evidence = calcular_evidencia(probabilidades_hipoteses, likelihoods[hipoteses[0]])

    # Atualizar probabilidades a posteriori
    probabilidades_posteriores = []
    for hipotese in hipoteses:
        likelihood = likelihoods[hipotese][0] ** resultados.count('Cara') * likelihoods[hipotese][1] ** resultados.count('Coroa')
        posterior = calcular_probabilidade_condicional(probabilidades_hipoteses[hipoteses.index(hipotese)], likelihood, evidence)
        probabilidades_posteriores.append(posterior)

    # Exibir resultados
    for hipotese, posterior in zip(hipoteses, probabilidades_posteriores):
        print(f"Probabilidade a posteriori de {hipotese}: {posterior:.2f}")

if __name__ == '__main__':
    main()