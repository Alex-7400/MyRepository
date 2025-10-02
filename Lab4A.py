# Class: CSE 1321L
# Section: B10
# Term: Fall Semester 2025
# Instructor: Austin Krusemark
# Name: Alejandro Ramirez Quezada
# Assignment: 4A

numGrade = float(input("Enter your grade: "))
if numGrade > 97 and numGrade < 100:
    print(f"Letter grade is: A+")
elif numGrade > 94 and numGrade <= 97:
    print(f"Letter grade is: A")
elif numGrade > 91 and numGrade <= 94:
    print(f"Letter grade is: A-")
elif numGrade > 88 and numGrade <= 91:
    print(f"Letter grade is: B+")
elif numGrade > 85 and numGrade <= 88:
    print(f"Letter grade is: B")
elif numGrade > 82 and numGrade <= 85:
    print(f"Letter grade is: B-")
elif numGrade > 79 and numGrade <= 82:
    print(f"Letter grade is: C+")
elif numGrade > 76 and numGrade <= 79:
    print(f"Letter grade is: C")
elif numGrade > 73 and numGrade <= 76:
    print(f"Letter grade is: C-")
elif numGrade > 70 and numGrade <= 73:
    print(f"Letter grade is: D+")
elif numGrade > 67 and numGrade <= 70:
    print(f"Letter grade is: D")
elif numGrade > 64 and numGrade <= 67:
    print(f"Letter grade is: D-")
elif numGrade < 64:
    print(f"Letter grade is: F")

