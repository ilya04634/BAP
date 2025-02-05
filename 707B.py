def find_minimum_delivery_cost():
    n, m, k = map(int, input().split())


    if k == 0 or k == n:
        print(-1)
        return

    roads = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        roads.append((u, v, l))

    storages = set(map(int, input().split()))

    min_cost = float('inf')

    for u, v, l in roads:
        if (u in storages and v not in storages) or (v in storages and u not in storages):
            min_cost = min(min_cost, l)

    print(min_cost if min_cost != float('inf') else -1)


find_minimum_delivery_cost()
