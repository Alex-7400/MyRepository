# Class: CSE 1321L
# Section: B10
# Term: Fall Semester 2025
# Instructor: Austin Krusemark
# Name: Alejandro Ramirez Quezada
# Assignment: 4B

print("Welcome!")
number = float(input("Please input a number: "))
choice = input("What would you like to do with this number: "
      "\n0) Get the additive inverse of the number"
      "\n1) Get the reciprocal of the number"
      "\n2) Square the number"
      "\n3) Cube the number"
      "\n4) Exit the program"
      "\n")
match choice:
    case "0":
        additive_inverse = -number
        print(f"The additive inverse of {number} is {additive_inverse}")
    case "1":
        if number == 0:
            print("Cannot divide by 0!")
        else:
            reciprocal = 1 / number
            print(f"The reciprocal of {number} is {round(reciprocal,3)}")
    case "2":
        square = number * number
        print(f"The square of {number} is {square}")
    case "3":
        cubed = number * number * number
        print(f"The cube of {number} is {cubed}")
    case "4":
        print("Thank you, goodbye!")
    case _:
        print("Invalid option!")