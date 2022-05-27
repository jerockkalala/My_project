# Assignment 8.1
# Jerock Kalala
# CIS-245 Introduction to Programming
# This program  creates a virtual garage by using inheritance to create a parent class and two child classes
# the program will prompt the user to create at least one object of each type (Car and Pickup)
# Using a menu system and capturing user input your program will allow the user the choice of adding a car
# or pickup truck and define the vehicle's attributes. The program uses user input to define the vehicle's attributes.

# Function outside the class
def read_car():
    car = {'make': '', 'model': '', 'doors': ''}
    make = input("Please enter the make of the vehicle: ")
    car['make'] = make.title()
    model = input("Please enter the make of the vehicle: ")
    car['model'] = model.title()
    car['doors'] = input("Please enter the number of doors: ")
    print("\nYou have successfully created a car. Here are the options you entered: ")
    return "The Make: "+car['make']+ ", \nThe Model: " + car['model'] + ", \nThe number of doors: " + car['doors']

def read_pickup():
    pick = {'make': '', 'model': '', 'bed_length': ''}
    make = input("Please enter the make of the vehicle: ")
    pick['make'] = make.title()
    model = input("Please enter the make of the vehicle: ")
    pick['model'] = model.title()
    pick['bed'] = input("Please enter the bed length: ")
    print("\nYou have successfully created a pickup. Here are the options you entered: ")
    return "The Make: " + pick['make'] + ", \nThe Model: " + pick['model'] + ", \nThe bed length: " + pick['bed']

def quit():
    print("Thank you for using my program")
    exit()

####################################################################################
# Create parent class Vehicle


class Vehicle:
    # initialization or Constructor
    def __init__(self):
        self.vehicle_option = {'make': '', 'model': ''}

        self.vehicle_option['make'] = input(print("Enter the make: "))
        self.vehicle_option['model'] = input(print("Enter the model: "))

    def set_make(self, make):
        self.vehicle_option['make'] = make

    def set_model(self, model):
        self.vehicle_option['model'] = model

# Function to get the Make and the model
    def get_make(self):
        self.make = self.vehicle_option['make']
        return self.make.title()

    def get_model(self):
        self.model = self.vehicle_option['model']
        return self.model.title()

# Function to display
    def display_options(self):
        print(f"\nYour vehicle has been successfully created. below are the details you provided: ")
        print(f"Make: {self.vehicle_option['make']}.")
        print(f"Model: {self.vehicle_option['model']}.")
        print("")


# Create Subclass car
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super.__init__(make, model)
        self.doors = doors

#  car subclass functions
    def getNum_doors(self):
        self.num_doors = input(print("Enter the number of doors: "))
        return self.num_doors

    def __str__(self):
        return "Successful added car: " + super(Car, self).__str__() + ", NumDoors: " + str(self.num_doors)


#  create Subclass Pickup
class Pickup(Vehicle):
    def __init__(self, make, model, bed_length):
        super.__init__(make, model)
        self.bed_length = bed_lengh

# subclass class pickup functions
    def getPickup(self):
        self.bed_length = input(print("Enter the length of the bed: "))
        return self.bed_length

    def __str__(self):
        return "Successful picked car: " + super(Car, self).__str__() + ", NumDoors: " + str(self.bed_length)


# Diver Code
print("\nWelcome to Jerock Garage\n")
while True:
    user_input = input(print("Please Enter 1 for car, 2 for pickup or 3 to quit the program: "))
    if user_input == '1':
        instance_1 = read_car()
        print(instance_1)
    elif user_input == '2':
        instance_1 = read_pickup()
        print(instance_1)
    elif user_input == '3':
        quit()
    else:
        print("The input is invalid. You can try again\n")

