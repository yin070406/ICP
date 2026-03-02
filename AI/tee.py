try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    print("You have entered a valid integer.")
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")