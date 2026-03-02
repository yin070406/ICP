array = []
matrix = []
index = 0
for n in range(1,10):
    num = int(input(f"9 integers for the 3x3 matrix [{n}]: "))
    array.append(num)
for i in range(0, 3):
    row = []
    for j in range(0, 3):
        row.append(array[index])
        index += 1
    matrix.append(row)
print(matrix)