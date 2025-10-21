#Student Name: Ng Tsz Yin
#Student ID: 20307097

fruit_stand = "Happy Fruit World"
slogan = "An apple a day keeps a doctor away!"
stand_address = "10 Main Street, Baltimore, Maryland"

star = "*" * 4
dotted_line = "-" * 50
units = "USD/kg"

fruits = ["Apple", "Pear", "Orange", "Coconut", "Watermelon"]
price = [1.29, 8.59, 4.99, 5.29, 3.20]

print(star + "\t" + fruit_stand + "\t" + star + "\n")
print(slogan)

print(fruits[0], f"{price[0]:.2f}", units, sep=" @ ")
print(fruits[1], f"{price[1]:.2f}", units, sep=" @ ")
print(fruits[2], f"{price[2]:.2f}", units, sep=" @ ")
print(fruits[3], f"{price[3]:.2f}", units, sep=" @ ")
print(fruits[4], f"{price[4]:.2f}", units, sep=" @ ")

print(dotted_line)
print(stand_address)