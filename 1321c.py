def max_deletions(s: str) -> int:
    s = list(s)
    deletions = 0
    while True:
        flag = False
        for ch in range(ord('z'), ord('a'), -1):
            c = chr(ch)
            for i in range(len(s)):
                if s[i] == c:
                    if (i > 0 and s[i - 1] == chr(ch - 1)) or (i < len(s) - 1 and s[i + 1] == chr(ch - 1)):
                        s.pop(i)
                        deletions += 1
                        flag = True
                        break
            if flag:
                break
        if not flag:
            break
    return deletions


n = int(input())
s = input().strip()

print(max_deletions(s))
