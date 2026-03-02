def split_SID(str1):
    result = []
    for i in range(0, len(str1)):
        result.append(str1[i])
    return result

def factor_pairs(int1):
    result = []
    for i in range(1, int1):
        if int1 % i == 0:
            j = int1 // i
            result.append([i, j])
            if i != j:
                result.append([j, i])
    return result

def reshape_1d_to_2d(lst, rows, cols):
    matrix = []
    index = 0
    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(lst[index])
            index += 1
        matrix.append(row)
    return matrix

def find_dimensions_2d_list(lst_2d):
    rows = len(lst_2d)
    cols = len(lst_2d[0])
    return [rows, cols]

def matrix_multiplication(matrix1, matrix2):
    row1 = len(matrix1)
    col1 = len(matrix1[0])
    row2 = len(matrix2)
    col2 = len(matrix2[0])
    result = []
    if col1 != row2:
        print("Invalid. The number of columns in the first matrix must equal the number of rows in the second matrix.")
    for i in range(row1):
        row = []
        for j in range(col2):
            total = 0
            for k in range(col1):
                total = int(matrix1[i][k]) * int(matrix2[k][j])
            row.append(total)
        result.append(row)
    return result

def main():
    my_sid = "12345678"
    new_sid = split_SID(my_sid)
    print(f"There are {len(new_sid)} items on the list.")
    print("Available reconstruction 2-D sizes (rows x columns):")
    demo_factor = factor_pairs(len(new_sid))
    for i,j in enumerate(demo_factor, 1):
        print(f"{i}: {j[0]} x {j[1]}")
    print()
    
    print(f"For demonstration, the integers will be hard coded to be reconstructed into a 2 x 4 matrix:")
    demo_2d = reshape_1d_to_2d(new_sid, 2, 4)
    print(demo_2d)
    print()

    sid = int(input("What is your student ID? "))
    split_sid = split_SID(str(sid))
    print(f"Your SID is {sid}, and after spliting it into individual integers, it becomes {split_sid}.")
    print(f"There are {len(split_sid)} items on the list.")
    print("Available reconstruction 2-D sizes (rows x columns): ")
    factor = factor_pairs(len(split_sid))
    for i,j in enumerate(factor, 1):
        print(f"{i}: {j[0]} x {j[1]}")
    print()

    choice = int(input("Please choose the option for reconstruction. Enter the integer representing that option: "))
    selected = factor[choice - 1]
    user_2d = reshape_1d_to_2d(split_sid, selected[0], selected[1])
    print(f"You selected option [{choice}], i.e., {selected}. The matrix becomes:")
    print(user_2d)
    print()

    print("Let's try performing matrix multiplication between the two matrices, 1st x 2nd ...")
    print()

    result = matrix_multiplication(demo_2d, user_2d)
    if result is None:
        print("Unfortunately, matrix multiplication cannot be processed; please try again using other student IDs or numbers.")
        print("Do not forget the size of the matrix also matters.")
        print("See you.")
    else:
        print("The resultant matrix is:")
        for i in range(0, len(result)-1):
            print(result[i])
        print()
        print("Congratulations.")
        print("This is the end of this programme, but you are welcome to try other student IDs or numbers.")

if __name__ == "__main__":
    main()