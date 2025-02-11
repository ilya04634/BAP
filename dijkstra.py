# def dijcstra(graph, start, end):
#     found = False
#     dist = 0
#
#     while found == False:
#
#         current_vertex = graph[start]
#         for i in range(1, len(current_vertex)):
#             n = start
#             if current_vertex[i] != end:
#                 if current_vertex[i] <= n:
#                     n

import heapq

def dijkstra(graph, start):
    shortest_paths = {vertex: float('inf') for vertex in graph}
    shortest_paths[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 8},
    'D': {'B': 10, 'C': 3, 'E': 6, 'F': 9},
    'E': {'C': 8, 'D': 6, 'F': 1},
    'F': {'D': 9, 'E': 1}
}


start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)


for vertex, distance in shortest_paths.items():
    print(f"путь от {start_vertex} до {vertex}: {distance}")


