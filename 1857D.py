import sys

t = int(sys.stdin.readline().strip())  

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    diff = [(a[i] - b[i], i + 1) for i in range(n)]

    max_diff = max(diff)[0]
    strong_vertices = sorted(i for d, i in diff if d == max_diff)

    print(len(strong_vertices))
    print(*strong_vertices)











