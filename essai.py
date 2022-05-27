#def auto(voiture, make):
#    """Display a simple greeting"""
#    print(f"this car: {voiture.title()}, {make}")

#def message():
#    print("In my house hold we have ", end="")

#message()
#auto(voiture='toyota', make='camry')

class Vehicle:
    # Constructor
    def __init__(self, make, model):
        self.make = make
        self.model = model
    # Getters
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}"


# Car class inherits from Vehicle
class Car(Vehicle):
    # Constructor
    def __init__(self, make, model, engineSize, numDoors):
        super().__init__(make, model)
        # Super class class
        # Initialize car's attributes
        self.engineSize = engineSize
        self.numDoors = numDoors

    # Functions
    def getEngineSize(self):
        return self.engineSize
    def getNumDoors(self):
        return self.numDoors
    def __str__(self):
        return  "CAR:==> "+super(Car, self).__str__() + ", Engine Size " + str(self.engineSize) + ", NumDoors: " + str(self.numDoors)

    # Pickup class inherits from Vehicle
class Pickup(Vehicle):
    def __init__(self, make, model, cabStyle, bedLength):
        super().__init__(make, model, )
        # Super class class
        # Initialize pickup's attributes
        self.cabStyle = cabStyle
        self.bedLength = bedLength
    # Functions
    def getCabStyle(self):
        return self.cabStyle
    def getBedLength(self):
        return self.bedLength
    def __str__(self):
        return "PICKUP:==> "+super(Pickup, self).__str__() + ", Cab Style " + str(self.cabStyle) + ", Bed Length: " + str(self.bedLength)

# Test code here
if __name__ == '__main__':
    garage = {'make', 'model', 'size', 'doors'}  # Take empty virtual garage
    # Prepare some vehicles
    car1 = Car("MAKE1", "MODEL1", "SIZE1", 4)
    car2 = Car("MAKE2", "MODEL2", "SIZE2", 2)
    car3 = Car("MAKE3", "MODEL3", "SIZE3", 6)

    pickup1 = Pickup("MAKE4", "MODEL4", "CAB STYLE1", "BED LENGTH1")
    pickup2 = Pickup("MAKE5", "MODEL5", "CAB STYLE2", "BED LENGTH2")
    pickup3 = Pickup("MAKE6", "MODEL6", "CAB STYLE3", "BED LENGTH3")
    # Add some vehicles to garage
    garage = [car1, pickup2, pickup3, car2, car3, pickup1]

    # Print the garage
    for vehicle in garage:
        print(vehicle)
    # Add some vehicles to garage
    garage = [pickup1, pickup2, pickup3, car1, car2, car3]

