# Class: CSE 1321L B10
# Section: 81000
# Term: Fall Semester 2025
# Instructor: Austin Krusemark
# Name: Alejandro Ramirez Quezada
# Lab: 3A - Calculator for minimum monthly payment on credit card.

CurBal = float (input("Amount owed: $"))
CurAPR = float (input("APR: "))

MonthlyP = (CurAPR / 12)
MinPay = round((MonthlyP /100) * CurBal,2)

print(f"Monthly percentage rate: {round(MonthlyP,3)}")
print(f"Minimum payment: ${MinPay}")