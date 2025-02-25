def find(parent, v):
    while parent[v] != v:
        v = parent[v]
    return v


def union(parent, rank, v1, v2):
    root1 = find(parent, v1)
    root2 = find(parent, v2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1


def kruskal(n, edges):
    edges.sort(key=lambda edge: edge[2])  # Сортируем рёбра по весу
    parent = list(range(n))  # Инициализируем массив родительских узлов
    rank = [0] * n  # Ранги для сжатия путей
    mst = []  # Минимальное остовное дерево

    for v1, v2, weight in edges:
        if find(parent, v1) != find(parent, v2):
            union(parent, rank, v1, v2)
            mst.append((v1, v2, weight))

    return mst


# Пример использования:
n = 5  # Количество вершин
graph = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5),
    (1, 3, 15), (2, 3, 4)
]

mst = kruskal(n, graph)
print("Минимальное остовное дерево:", mst)
