class Students:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}\n")

s1 = Students("Alice", 101, [85, 90, 88])
s2 = Students("Bob", 102, [78, 82, 80])

# Displaying
s1.display()
s2.display()