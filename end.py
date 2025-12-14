rows = int(input("Enter the number of rows: "))
for i in range(0, rows):
    for j in range(0, rows):
        if i < j:
            print("x", end="")
        elif i == j:
            print("/", end="")
        else:
            print("o", end="")
    print()