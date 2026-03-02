student_info = {
    "Adrian": "B",
    "Aika": "A",
    "Casper": "A",
    "CC": "D",
    "Dickson": "C",
    "FongSnow": "B"
}

for name, grade in student_info.items():
    if student_info[name] == "A":
        print(name)

student_info["CC"] = "D"
print("The grade of Student 'CC' has been changed.")
for name, grade in student_info.items():
    if name == "CC":
        print(f"{name}: {grade}")

del student_info["FongSnow"]
print("The information of Student 'FongSnow' has been deleted.")

