# Class: CSE 1321L B10
# Section: 81000
# Term: Fall Semester 2025
# Instructor: Austin Krusemark
# Name: Alejandro Ramirez Quezada
# Lab: 3B - GPA Calculator

Crse1H = int (input("Course 1 hours: "))
Crse1G = int (input("Grade for course 1: "))
Crse2H = int (input("Course 2 hours: "))
Crse2G = int (input("Grade for course 2: "))
Crse3H = int (input("Course 3 hours: "))
Crse3G = int (input("Grade for course 3: "))
Crse4H = int (input("Course 4 hours: "))
Crse4G = int (input("Grade for course 4: "))

totalHrs = Crse1H + Crse2H + Crse3H + Crse4H
totalQP = ((Crse1G * Crse1H) + (Crse2G * Crse2H) + (Crse3G * Crse3H) + (Crse4G * Crse4H))
GPA = float(totalQP/totalHrs)

print("Total hours: " + str(totalHrs))
print("Total quality points: " + str(totalQP))
print(f"Your GPA for this semester is {round(GPA,2)}")
