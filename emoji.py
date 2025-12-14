while True:
    text = input("Please enter a line of text (enter 'bye' to quit the program): ")
    if text.lower() == "bye":
        print("see you next time")
        break

    output = ""
    for i in text:
        if i == "h" or i == "H":
            output += ":-)"
        elif i == "c" or i == "C":
            output += ":’("
        elif i == "a" or i == "A":
            output += "*^*"
        else:
            output += i

    print(output)