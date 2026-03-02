import heapq

def dijkstra(graph, start, end):
    """
    Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto
    entre dois nós em um grafo ponderado.

    :param graph: Um dicionário onde as chaves são os nós e os valores são listas
                  de tuplas (vizinho, peso).
    :param start: O nó de início.
    :param end: O nó de destino.
    :return: Uma lista contendo o caminho mais curto de start a end, ou None se
             não houver caminho.
    """
    # Inicializa as estruturas de dados
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        # Pega o nó com a menor distância
        current_distance, current_node, path = heapq.heappop(priority_queue)

        # Se o nó já foi visitado, pula para o próximo
        if current_node in visited:
            continue

        # Marca o nó como visitado
        visited.add(current_node)
        path = path + [current_node]

        # Se chegou ao destino, retorna o caminho
        if current_node == end:
            return path

        # Explora os vizinhos
        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_distance + weight, neighbor, path))

    # Se não há caminho para o destino
    return None

def main():
    """
    Função principal que define um grafo simples e encontra o caminho mais
    curto entre dois nós usando o algoritmo de Dijkstra.
    """
    # Exemplo de grafo simples
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_node = 'A'
    end_node = 'D'

    shortest_path = dijkstra(graph, start_node, end_node)

    if shortest_path:
        print(f'Caminho mais curto de {start_node} a {end_node}: {shortest_path}')
    else:
        print(f'Não há caminho de {start_node} a {end_node}.')

if __name__ == '__main__':
    main()