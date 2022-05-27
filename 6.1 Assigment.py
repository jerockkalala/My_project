# Assignment 6.1
# Jerock Kalala
# CIS-245 Introduction to Programming
# This program uses a function to convert the number of miles driven into kilometer
# it takes input form the user and convert it

# Function definition
def converter(value):
    km=value * 1.6
    return km

# Validation of imput
while True:
    try:
        print("please enter the the number of miles driven that you want to convert in Kilometer: ")
        distance=float(input())
        break
    except ValueError:
        print("the value you entered is not valid. Please re-enter a number of driven miles!")

""" Function call"""
kilo=converter(value=distance)

'''print the result'''
print(f"the number of miles driven is : {distance}, and the correspondent value in kilometer is {kilo} Kilometers.\n")


