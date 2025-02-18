import sys
from collections import deque


def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    if n % 2 != 0:
        print(-1)
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    subtree_size = [0] * (n + 1)
    result = 0

    stack = [(1, -1, False)]
    while stack:
        u, parent, visited = stack.pop()
        if visited:
            for v in adj[u]:
                if v != parent:
                    subtree_size[u] += subtree_size[v]
            if subtree_size[u] % 2 == 0 and u != 1:
                result += 1
        else:
            stack.append((u, parent, True))
            for v in adj[u]:
                if v != parent:
                    stack.append((v, u, False))
            subtree_size[u] = 1

    print(result)


if __name__ == "__main__":
    main()