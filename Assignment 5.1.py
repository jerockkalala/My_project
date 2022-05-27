# Assignment 5.1
# Jerock Kalala
# CIS-245 Introduction to Programming
# This program uses a while loop to determine how long
# it takes for an investment to double at a given interest rate

#Get the initiale amount ant the annual interest rate from the user
i_amount = float(input("please enter your initial investment: "))
an_rate = float(input("please enter the annual interest rate : "))

#Set the targetted amount
target = i_amount * 2
#Set the total amount equals to the initial amount and initialize the counter
tot_amount = i_amount
year_count = 0
#Define the while loop condition
while tot_amount < target:
    tot_amount = (tot_amount + (tot_amount * (an_rate/100)))
    year_count = year_count + 1
#Print the resul
print(f"The double of your initial amount invested should be: {target}")
print(f"\nWith a fixed annual interest rate of {an_rate} %, it will take about {year_count} years" ,end = ' ')
print(f"for your investment of {i_amount} to double")
