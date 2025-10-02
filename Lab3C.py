# Class: CSE 1321L B10
# Section: 81000
# Term: Fall Semester 2025
# Instructor: Austin Krusemark
# Name: Alejandro Ramirez Quezada
# Lab: 3C - Sandwich cooking calculator

SMt = 30 #seconds
MDt = 60 #seconds
LGt = 75 #seconds or 1 minute 15 seconds
XLt = 135 #seconds or 2 minutes 15 seconds

SMsndw = int (input("Enter the number of small sandwiches: "))
MDsndw = int (input("Enter the number of medium sandwiches: "))
LGsndw = int (input("Enter the number of large sandwiches: "))
XLsndw = int (input("Enter the number of extra-large sandwiches: "))

totalSecs = (SMsndw * SMt) + (MDsndw * MDt) + (LGsndw * LGt) + (XLsndw * XLt)
tCM, tCS = divmod(totalSecs, 60)
#tCM =
#tCS = 10

print("You've entered " + str(SMsndw) + " small sandwiches. ")
print("You've entered " + str(MDsndw) + " medium sandwiches.")
print("You've entered " + str(LGsndw) + " large sandwiches.")
print("You've entered " + str(XLsndw) + " extra-large sandwiches.")

print("Total cooking time is " + str(tCM) +" minutes and " + str(tCS) + " seconds.")