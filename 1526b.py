# n = int(input())
# for i in range(n):
#     m = input().split()
#     dig_count = len(str(m))
#     print(dig_count)


def main(x):
    m = x//111
    for b in range(1+m):
        a = x - 111*b
        if a%11==0:
            return True
    return False

t = int(input())
for i in range(t):
    x = int(input())
    if main(x):
        print("YES")
    else:
        print("NO")


# n = int(input())
# for i in range(n):
#     m = input()

