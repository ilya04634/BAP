def can_transport(graph, N, S, T, weight_limit):
    queue = [S]
    visited = set([S])
    front = 0

    while front < len(queue):
        node = queue[front]
        front += 1

        if node == T:
            return True

        for neighbor, weight in graph[node]:
            if neighbor not in visited and weight >= weight_limit:
                visited.add(neighbor)
                queue.append(neighbor)

    return False

def max_transport_weight(N, M, roads, S, T):

    graph = {i: [] for i in range(1, N + 1)}
    weights = []


    for A, B, W in roads:
        graph[A].append((B, W))
        weights.append(W)


    weights = sorted(set(weights))

    left, right = 0, len(weights) - 1
    best_weight = 0

    while left <= right:
        mid = (left + right) // 2
        test_weight = weights[mid]

        if can_transport(graph, N, S, T, test_weight):
            best_weight = test_weight
            left = mid + 1
        else:
            right = mid - 1

    return best_weight


N, M = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())


result = max_transport_weight(N, M, roads, S, T)


print(result)



# 4 5
# 1 2 30
# 2 3 20
# 3 4 10
# 1 3 25
# 2 4 15
# 1 4