# def convert(ls):
#     converted = []
#     for i in range(len(ls)):
#         if ls[i] == 'A':
#             converted.append(0)
#         elif ls[i] == 'B':
#             converted.append(1)
#         elif ls[i] == 'C':
#             converted.append(2)
#         elif ls[i] == 'D':
#             converted.append(3)
#         else:
#             converted.append(4)
#     return converted
#
# def swap_num(converted):
#     n = len(converted)
#
#     for i in range(n):
#         current = converted[i]
#         larger_right = False
#         for j in range(i+1, n):
#             if converted[j]>current:
#                 larger_right = True
#                 break
#             if


# def get_value(c):
#     return {'A': 1, 'B': 10, 'C': 100, 'D': 1000, 'E': 10000}[c]
#
# def calculate_value(s):
#     n = len(s)
#     has_larger_right = [False] * n
#     max_right = 0
#     for i in range(n - 1, -1, -1):
#         current_value = get_value(s[i])
#         if current_value < max_right:
#             has_larger_right[i] = True
#         max_right = max(max_right, current_value)
#
#     value = 0
#     for i in range(n):
#         current_value = get_value(s[i])
#         if has_larger_right[i]:
#             value -= current_value
#         else:
#             value += current_value
#     return value
#
# def max_value_after_replacement(s):
#     n = len(s)
#     max_value = calculate_value(s)
#
#
#     for i in range(n):
#         original_char = s[i]
#         for new_char in ['A', 'B', 'C', 'D', 'E']:
#             if new_char == original_char:
#                 continue
#             new_s = s[:i] + new_char + s[i+1:]
#             new_value = calculate_value(new_s)
#             if new_value > max_value:
#                 max_value = new_value
#
#     return max_value
#
# t = int(input())
# for _ in range(t):
#     s = input().strip()
#     print(max_value_after_replacement(s))
#
#
#
#
#

def calculate(s):
    a = b = c = d = e = False
    total = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'A':
            a = True
            total += -1 if (b or c or d or e) else 1
        elif s[i] == 'B':
            b = True
            total += -10 if (c or d or e) else 10
        elif s[i] == 'C':
            c = True
            total += -100 if (d or e) else 100
        elif s[i] == 'D':
            d = True
            total += -1000 if e else 1000
        elif s[i] == 'E':
            e = True
            total += 10000

    return total


def main():
    t = int(input())

    for _ in range(t):
        s = list(input())
        indices = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1}

        for i, char in enumerate(s):
            if indices[char] == -1:
                indices[char] = i

        res = calculate(s)

        for char, index in indices.items():
            if index != -1:
                for replacement in 'ABCDE':
                    if replacement != char:
                        s[index] = replacement
                        res = max(res, calculate(s))
                s[index] = char

        indices = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1}

        for i in range(len(s) - 1, -1, -1):
            if indices[s[i]] == -1:
                indices[s[i]] = i

        for char, index in indices.items():
            if index != -1:
                for replacement in 'ABCDE':
                    if replacement != char:
                        s[index] = replacement
                        res = max(res, calculate(s))
                s[index] = char

        print(res)


if __name__ == "__main__":
    main()







