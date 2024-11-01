x_arr_float = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
y_arr_float = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]


arr_float = [
    [47, 34, 54, 2, 643, 45],
    [8, 34, 554, 2, 64, 45],
    [4, 78, 5, 2, 43, 45],
    [6, 3, 8, 2, 63, 45],
    [94, 4, 54, 2, 3, 9],
    [47, 6, 5654, 2, 643, 5],
]

arr_int = [
    [47, 44, 54, 2, 643, 45],
    [8, 34, 554, 2, 64, 45],
    [4, 78, 8, 2, 43, 45],
    [6, 3, 8, 2, 63, 45],
    [94, 4, 54, 32, 3, 9],
    [47, 46, 5654, 2, 643, 5],
]

# def add_num(a, x, y, matrix):
#     matrix[x][y] = a
# def del_num(a, x, y, matrix):
#     matrix[x][y] = 0
print('1.show value \n'
      '2.change value \n'
      '3.delete value \n'
      '4.show whole the matrix'
)
choice = int(input(': '))
if choice != 4:
    x, y = input("enter x and y: ").split()
    if isinstance(x, str) and isinstance(y, str):
        x, y = int(x), int(y)

        if choice == 1:
            print(arr_int[x][y])

        elif choice == 2:
            b = int(input("enter number which you want to appropriate: "))
            arr_int[x][y] = b
            print(arr_int[x][y])
        elif choice == 3:
            arr_int[x][y] = 0

    else:
        if choice == 1:
            print(arr_float[x][y])

        elif choice == 2:
            b = int(input("enter number which you want to appropriate: "))
            arr_float[x][y] = b
        elif choice == 3:
            arr_float[x][y] = 0

input()












