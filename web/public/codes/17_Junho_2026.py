import sys

def calcular_percentil_imc(peso, altura, idade, sexo):
    """
    Calcula o percentil do IMC para crianças e adolescentes.
    
    Args:
        peso (float): Peso da criança ou adolescente em kg.
        altura (float): Altura da criança ou adolescente em metros.
        idade (int): Idade da criança ou adolescente em anos.
        sexo (str): Sexo da criança ou adolescente ('M' para masculino, 'F' para feminino).
    
    Returns:
        str: Percentil do IMC ou mensagem de erro.
    """
    # Tabelas de percentil simplificadas (apenas para exemplo)
    # Em um cenário real, essas tabelas seriam mais detalhadas e precisas
    percentil = {
        'M': {
            2: [12.4, 13.8, 15.3, 16.7, 18.1, 19.5, 20.9, 22.3, 23.7, 25.1],
            3: [12.7, 14.1, 15.6, 17.1, 18.6, 20.1, 21.6, 23.1, 24.6, 26.1],
            # ... (continuar para todas as idades até 18 anos)
        },
        'F': {
            2: [13.9, 15.3, 16.8, 18.2, 19.7, 21.2, 22.7, 24.2, 25.7, 27.2],
            3: [14.2, 15.7, 17.2, 18.7, 20.2, 21.7, 23.2, 24.7, 26.2, 27.7],
            # ... (continuar para todas as idades até 18 anos)
        }
    }
    
    try:
        # Cálculo do IMC
        imc = peso / (altura ** 2)
        
        # Encontrar o percentil aproximado (exemplo simplificado)
        if idade in percentil[sexo]:
            percentil_values = percentil[sexo][idade]
            for i, value in enumerate(percentil_values):
                if imc < value:
                    return f"Percentil aproximado: {i * 10}%"
            return "Percentil aproximado: 100%"
        else:
            return "Idade fora do intervalo suportado."
    except ZeroDivisionError:
        return "Altura não pode ser zero."
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

def main():
    """
    Função principal para execução do script.
    """
    if len(sys.argv) != 5:
        print("Uso: python calculadora_imc_infantil.py <peso> <altura> <idade> <sexo>")
        sys.exit(1)
    
    peso = float(sys.argv[1])
    altura = float(sys.argv[2])
    idade = int(sys.argv[3])
    sexo = sys.argv[4].upper()
    
    resultado = calcular_percentil_imc(peso, altura, idade, sexo)
    print(resultado)

if __name__ == '__main__':
    main()