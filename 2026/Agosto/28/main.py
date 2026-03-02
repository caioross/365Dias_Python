import random

class Bioma:
    def __init__(self, nome, temperatura_media, umidade_media):
        self.nome = nome
        self.temperatura_media = temperatura_media
        self.umidade_media = umidade_media

    def gera_clima(self):
        temperatura = random.gauss(self.temperatura_media, 5)
        umidade = random.gauss(self.umidade_media, 20)
        return temperatura, umidade

def cria_biomas():
    biomas = [
        Bioma("Deserto", 30, 20),
        Bioma("Floresta Tropical", 25, 80),
        Bioma("Tundra", -10, 30),
        Bioma("Selva", 20, 70),
        Bioma("Deserto Polar", -5, 10)
    ]
    return biomas

def main():
    biomas = cria_biomas()
    for bioma in biomas:
        temperatura, umidade = bioma.gera_clima()
        print(f"Bioma: {bioma.nome}")
        print(f"Temperatura: {temperatura:.2f}°C")
        print(f"Umidade: {umidade:.2f}%")
        print("-" * 20)

if __name__ == '__main__':
    main()