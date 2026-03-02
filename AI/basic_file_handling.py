import os
with open("input.txt", "r") as f:
    content = f.read()

lines = content.count("\n")+1 if content else 0
words = len(content.split())
characters = len(content)

f2 = open("summary.txt", "x")

with open("summary.txt", "w") as f2:
    f2.write(f"Lines: {lines}\n")
    f2.write(f"Words: {words}\n")
    f2.write(f"Characters: {characters}")

print("Summary written to summary.txt")
