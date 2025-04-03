import sys
from sys import stdin


def main():
    sys.setrecursionlimit(1 << 25)
    n, m = map(int, stdin.readline().split())
    parent = [i for i in range(n + 1)]
    size = [1] * (n + 1)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if size[u_root] > size[v_root]:
            parent[v_root] = u_root
            size[u_root] += size[v_root]
        else:
            parent[u_root] = v_root
            size[v_root] += size[u_root]

    for _ in range(m):
        parts = list(map(int, stdin.readline().split()))
        ki = parts[0]
        if ki == 0:
            continue
        first = parts[1]
        for num in parts[2:]:
            union(first, num)

    res = []
    for i in range(1, n + 1):
        res.append(str(size[find(i)]))
    print(' '.join(res))


if __name__ == '__main__':
    main()