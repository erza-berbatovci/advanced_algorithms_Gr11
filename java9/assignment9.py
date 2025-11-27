import heapq

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 2},
    'F': {'D': 6, 'E': 2, 'G': 1},
    'G': {'F': 1, 'H': 3},
    'H': {'G': 3, 'I': 2, 'J': 6},
    'I': {'H': 2, 'J': 1},
    'J': {'H': 6, 'I': 1}
}

def dijkstra(graph, start, end):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))
    
    path = []
    node = end
    while node:
        path.append(node)
        node = previous[node]
    path.reverse()
    
    return path, distances[end]

shortest_path, distance = dijkstra(graph, 'A', 'J')
print("Rruga më e shkurtër:", shortest_path)
print("Distanca totale:", distance)
