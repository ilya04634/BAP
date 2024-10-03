def encryption(n,ls):
    if n<=0:
        return ls

    m = n % 2
    n //= 2
    ls.insert(0, m)
    return encryption(n,ls)


def decryption(ls):
    ls.reverse()
    n = 0
    for i in range(len(ls)):
        n += ls[i]*2**i
    return n

h = int(input("Enter a number: "))
bin = []
j = encryption(h,bin)
print(j)

i = decryption(j)
print(i)