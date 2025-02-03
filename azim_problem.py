import random

rows, cols = 10, 10

matrix = [random.randint(10, 99) for _ in range(rows * cols)]
print(matrix)


def set_value(matrix, row, col, value):
    matrix[row * cols + col] = value

def get_value(matrix, row, col):
    return matrix[row * cols + col]

u_row, u_col = int(input("choice row: ")), int(input("choice cal: "))
u_value = int(input("input value: "))

set_value(matrix, u_row, u_col, u_value)


for i in range(rows):
    row = [get_value(matrix, i, j) for j in range(cols)]
    print(row)