import random

class Personagem:
    """
    Classe que representa um personagem no jogo de RPG.
    
    Atributos:
    - nome (str): Nome do personagem.
    - força (int): Valor de força do personagem.
    - sorte (int): Valor de sorte do personagem.
    """
    
    def __init__(self, nome, força, sorte):
        self.nome = nome
        self.força = força
        self.sorte = sorte

    def atacar(self, alvo):
        """
        Método que simula o ataque do personagem ao alvo.
        
        Args:
        - alvo (Personagem): Personagem que será atacado.
        
        Returns:
        - bool: True se o ataque for bem-sucedido, False caso contrário.
        """
        precisão = random.randint(1, 20) + self.sorte
        if precisão > 15:
            dano = random.randint(1, 10) + self.força
            alvo.força -= dano
            print(f"{self.nome} ataca {alvo.nome} com sucesso, causando {dano} de dano!")
            return True
        else:
            print(f"{self.nome} falha ao atacar {alvo.nome}.")
            return False

def main():
    """
    Função principal que simula um combate entre dois personagens.
    """
    personagem1 = Personagem("Guerreiro", 15, 10)
    personagem2 = Personagem("Mago", 10, 15)
    
    print(f"Combate entre {personagem1.nome} e {personagem2.nome}!")
    
    turno = 1
    while personagem1.força > 0 and personagem2.força > 0:
        print(f"\nTurno {turno}:")
        if turno % 2 == 1:
            personagem1.atacar(personagem2)
        else:
            personagem2.atacar(personagem1)
        
        if personagem1.força <= 0:
            print(f"\n{personagem2.nome} vence o combate!")
        elif personagem2.força <= 0:
            print(f"\n{personagem1.nome} vence o combate!")
        
        turno += 1

if __name__ == '__main__':
    main()