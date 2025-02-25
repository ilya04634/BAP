import sys

def is_valid_rearrangement(n, a):
    occupied = set()
    for i in range(n):
        new_room = (i + a[i] % n + n) % n
        if new_room in occupied:
            return "NO"
        occupied.add(new_room)
    return "YES"

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        results.append(is_valid_rearrangement(n, a))
    print("\n".join(results))

if __name__ == "__main__":
    main()