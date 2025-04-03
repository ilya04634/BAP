import sys


def max_weapons(p, f, cnts, cntw, s, w):
    if s > w:
        cnts, cntw, s, w = cntw, cnts, w, s

    max_count = 0

    for swords_taken in range(min(cnts, p // s) + 1):
        remaining_p = p - swords_taken * s
        axes_taken = min(cntw, remaining_p // w)

        remaining_swords = cnts - swords_taken
        remaining_axes = cntw - axes_taken

        swords_taken_f = min(remaining_swords, f // s)
        remaining_f = f - swords_taken_f * s
        axes_taken_f = min(remaining_axes, remaining_f // w)

        total_weapons = swords_taken + axes_taken + swords_taken_f + axes_taken_f
        max_count = max(max_count, total_weapons)

    return max_count


def main():
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        p, f = map(int, data[index:index + 2])
        index += 2
        cnts, cntw = map(int, data[index:index + 2])
        index += 2
        s, w = map(int, data[index:index + 2])
        index += 2

        results.append(str(max_weapons(p, f, cnts, cntw, s, w)))

    print("\n".join(results))


if __name__ == "__main__":
    main()