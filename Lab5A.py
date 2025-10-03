# Class: CSE 1321L
# Term: Fall Semester 2025
# Assignment: 5A - Largest of 10

print("Please enter 10 numbers and this program will display the largest.")
a= 0
bigNum = 0
for i in range(1, 11):
    a += 1
    curNum = int(input(f"Please enter number {a}: "))
    if curNum >= bigNum:
        bigNum = curNum
print("The largest number was",bigNum)