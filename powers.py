
n, x = int(input(": ")), int(input(": "))
a = n*x
a %=4

if a ==1:
    print(2)
elif a ==2:
    print(4)
elif a ==3:
    print(8)
else:
    print(6)