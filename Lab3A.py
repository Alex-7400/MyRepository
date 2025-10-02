# Class: CSE 1321L
# Term: Fall Semester 2025
# Lab: 3A - Calculator for minimum monthly payment on credit card.

CurBal = float (input("Amount owed: $")) # Asks for Ammount owed
CurAPR = float (input("APR: ")) #Asks for APR

MonthlyP = (CurAPR / 12) # Calculates monthly percentage: Divide current APR by 12
MinPay = round((MonthlyP /100) * CurBal,2) # Calculates Minimum payment

print(f"Monthly percentage rate: {round(MonthlyP,3)}") # Prints Monthly percentage rate

print(f"Minimum payment: ${MinPay}") # Prints Minimum payment
