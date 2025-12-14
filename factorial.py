def getFactorial(n):
    total = 1
    total_list = []
    if n == 0 or n == 1:
        return total
    if n < 0:
        return []
    for i in range(1, n+1):
        total *= i
        total_list.append(total)
    return total_list

def dispFactorialNumList(fList):
    fList.sort()
    for i,j in enumerate(fList):
        print(f"n = {i} => n! = {j}")

def main():
    num = int(input("Please enter an integer: "))
    print("Factorial numbers are:")
    print("-"*20)
    if num < 0:
        print("No factorial numbers")
    else:
        fList = getFactorial(num)
        dispFactorialNumList(fList)
    print("-"*20)

if __name__ == "__main__":
    main()