"""
simulador_cache_lru.py

Este script demonstra o funcionamento do algoritmo de substituição de cache "Least Recently Used (LRU)".
O LRU é um método de substituição de páginas que remove a página que foi menos usada recentemente.

Classes:
    - LRUCache: Implementa a lógica do cache LRU.

Funções:
    - main: Função principal que demonstra o uso da classe LRUCache.

"""

from collections import OrderedDict

class LRUCache:
    """
    Implementação de um cache LRU (Least Recently Used).

    Atributos:
        capacity (int): A capacidade máxima do cache.
        cache (OrderedDict): Estrutura de dados que armazena as páginas do cache.
    """

    def __init__(self, capacity: int):
        """
        Inicializa a instância do cache LRU.

        Args:
            capacity (int): A capacidade máxima do cache.
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """
        Obtém o valor associado à chave especificada.

        Se a chave estiver no cache, ela é movida para o final para indicar que foi recentemente usada.
        Se a chave não estiver no cache, retorna -1.

        Args:
            key (int): A chave a ser buscada no cache.

        Returns:
            int: O valor associado à chave, ou -1 se a chave não estiver no cache.
        """
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Insere um valor associado a uma chave no cache.

        Se a chave já estiver no cache, seu valor é atualizado e a chave é movida para o final.
        Se a chave não estiver no cache e o cache está cheio, a página menos recentemente usada é removida.
        A chave e o valor são então inseridos no cache.

        Args:
            key (int): A chave a ser inserida no cache.
            value (int): O valor associado à chave.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

def main():
    """
    Função principal que demonstra o uso da classe LRUCache.
    """
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # Retorna 1
    cache.put(3, 3)       # Remove a chave 2
    print(cache.get(2))  # Retorna -1 (não está no cache)
    cache.put(4, 4)       # Remove a chave 1
    print(cache.get(1))  # Retorna -1 (não está no cache)
    print(cache.get(3))  # Retorna 3
    print(cache.get(4))  # Retorna 4

if __name__ == '__main__':
    main()