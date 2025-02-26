

def main(t):
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = set()
        for j in range(n):
            s.add((j+a[j])%n)
        print("YES" if len(s) == n else "NO")

if __name__ == '__main__':
    t = int(input())
    main(t)