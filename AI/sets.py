integers = set()
for i in range(0, 5):
    num = int(input("Numbers: "))
    integers.add(num)
print(integers)

new_tuple = tuple(integers)
sort = sorted(new_tuple)

print(f"Sets: {integers}")
print(f"Tuple: {new_tuple}")
print(f"Sorted tuple: {sort}")