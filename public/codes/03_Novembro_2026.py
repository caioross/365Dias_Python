import math

def volume_cone(raio, altura):
    """Calcula o volume de um cone."""
    return (1/3) * math.pi * raio**2 * altura

def area_superficie_cone(raio, altura):
    """Calcula a área de superfície de um cone."""
    geratriz = math.sqrt(raio**2 + altura**2)
    return math.pi * raio * (raio + geratriz)

def volume_cilindro(raio, altura):
    """Calcula o volume de um cilindro."""
    return math.pi * raio**2 * altura

def area_superficie_cilindro(raio, altura):
    """Calcula a área de superfície de um cilindro."""
    return 2 * math.pi * raio * (raio + altura)

def volume_prisma(base_area, altura):
    """Calcula o volume de um prisma."""
    return base_area * altura

def area_superficie_prisma(perimetro_base, altura, base_area):
    """Calcula a área de superfície de um prisma."""
    return 2 * base_area + perimetro_base * altura

def volume_piramide(base_area, altura):
    """Calcula o volume de uma pirâmide."""
    return (1/3) * base_area * altura

def area_superficie_piramide(perimetro_base, altura, base_area):
    """Calcula a área de superfície de uma pirâmide."""
    area_lateral = (perimetro_base * altura) / 2
    return base_area + area_lateral

def main():
    print("Calculadora de Geometria 3D")
    print("Escolha a figura geométrica:")
    print("1. Cone")
    print("2. Cilindro")
    print("3. Prisma")
    print("4. Pirâmide")
    
    escolha = input("Digite a opção (1-4): ")
    
    if escolha == '1':
        raio = float(input("Digite o raio do cone: "))
        altura = float(input("Digite a altura do cone: "))
        print(f"Volume do cone: {volume_cone(raio, altura):.2f}")
        print(f"Área de superfície do cone: {area_superficie_cone(raio, altura):.2f}")
    elif escolha == '2':
        raio = float(input("Digite o raio do cilindro: "))
        altura = float(input("Digite a altura do cilindro: "))
        print(f"Volume do cilindro: {volume_cilindro(raio, altura):.2f}")
        print(f"Área de superfície do cilindro: {area_superficie_cilindro(raio, altura):.2f}")
    elif escolha == '3':
        base_area = float(input("Digite a área da base do prisma: "))
        altura = float(input("Digite a altura do prisma: "))
        perimetro_base = float(input("Digite o perímetro da base do prisma: "))
        print(f"Volume do prisma: {volume_prisma(base_area, altura):.2f}")
        print(f"Área de superfície do prisma: {area_superficie_prisma(perimetro_base, altura, base_area):.2f}")
    elif escolha == '4':
        base_area = float(input("Digite a área da base da pirâmide: "))
        altura = float(input("Digite a altura da pirâmide: "))
        perimetro_base = float(input("Digite o perímetro da base da pirâmide: "))
        print(f"Volume da pirâmide: {volume_piramide(base_area, altura):.2f}")
        print(f"Área de superfície da pirâmide: {area_superficie_piramide(perimetro_base, altura, base_area):.2f}")
    else:
        print("Opção inválida.")

if __name__ == '__main__':
    main()