def build_cycle_graph(n):
    if n < 3:
        raise ValueError("Минимальное количество вершин в таком графе — 3")

    graph = {i: (i + 1) % n for i in range(n)}
    return graph


def check_graph(graph):
    n = len(graph)
    incoming_edges = {i: 0 for i in range(n)}

    for v_from, v_to in graph.items():
        incoming_edges[v_to] += 1

    return all(deg == 1 for deg in incoming_edges.values())



n = 9
cycle_graph = build_cycle_graph(n)


print("Граф:", cycle_graph)


if check_graph(cycle_graph):
    print(f"Граф с {n} вершинами удовлетворяет условиям.")
else:
    print(f"Граф с {n} вершинами не удовлетворяет условиям.")
