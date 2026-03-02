def find_lcm(num1, num2):
    if num1 > num2:
        greater = num1
        smaller = num2
    else:
        greater = num2
        smaller = num1
    remainder = greater % smaller
    while (remainder != 0):
        greater = smaller
        smaller = remainder
        remainder = greater % smaller
    gcd = smaller

    lcm = int((int(num1) * int(num2))) / int(gcd)
    return lcm

def find_hcf(num1, num2):
        if num1 > num2:
            greater = num1
            smaller = num2
        else:
            greater = num2
            smaller = num1
        remainder = greater % smaller
        while (remainder != 0):
            greater = smaller
            smaller = remainder
            remainder = greater % smaller
        gcd = smaller
        return gcd

l = [2, 7, 3, 9, 4]

num1 = l[0]        # first number
num2 = l[1]        # second number
lcm = find_lcm(num1, num2)   # LCM of first two
hcf = find_hcf(num1, num2)

for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i]) 
    hcf = find_hcf(hcf, l[i])

print(f"LCM of the list: {lcm}")
print(f"HCF of the list: {hcf}")
