total = 1
n = int(input(""))
if n == 0 or n == 1:
    print(total)
else:
    for i in range(1, n+1):
        total *= i
print(total)