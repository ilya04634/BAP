def floyd_warshall(n, edges):

    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    next = [[-1] * n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0

    for u, v, w in edges:
        dist[u][v] = w
        next[u][v] = v

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    return dist, next

def reconstruct_path(start, end, next):
    if next[start][end] == -1:
        return []
    path = [start]
    while start != end:
        start = next[start][end]
        path.append(start)
    return path

# Пример использования
if __name__ == "__main__":
    n = 4
    edges = [
        (0, 1, 3),
        (0, 2, 6),
        (1, 2, 2),
        (2, 3, 1),
        (3, 0, 1)
    ]

    dist, next = floyd_warshall(n, edges)

    print("Матрица расстояний:")
    for row in dist:
        print(row)

    print("\nПути:")
    for i in range(n):
        for j in range(n):
            if i != j:
                path = reconstruct_path(i, j, next)
                if path:
                    print(f"Путь от {i} до {j}: {' -> '.join(map(str, path))}, стоимость: {dist[i][j]}")
                else:
                    print(f"Пути от {i} до {j} не существует")