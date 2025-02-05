
t = int(input())
for _ in range(t):
    n = int(input())
    used = [False] * (n + 1)
    princess = 0
    for i in range(1, n + 1):
        preferences = list(map(int, input().split()))
        k = preferences[0]
        found = False
        for j in range(1, k + 1):
            if not used[preferences[j]]:
                used[preferences[j]] = True
                found = True
                break
        if not found:
            princess = i
    if princess == 0:
        print("OPTIMAL")
    else:
        prince = 1
        while prince <= n and used[prince]:
            prince += 1
        print("IMPROVE")
        print(princess, prince)

