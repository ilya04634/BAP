def get_value(c):
    m = {'N': 0, 'E': 1, 'S': 2, 'W': 3}[c]
    return m

def main(n, ls):
    count = 1
    curent_pos = get_value(ls[0])
    for i in range(1, n):
        value = get_value(ls[i])
        if abs(curent_pos - value) == 1 or abs(curent_pos - value) == 3:
            curent_pos = value
            count += 1

        elif abs(curent_pos - value) > 1:
            curent_pos += 1

    return count

n = int(input())
ls = list(input().strip())

print(main(n, ls))


