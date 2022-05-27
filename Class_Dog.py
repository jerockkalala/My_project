class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is  rolled over!")

#Creating a instance of class Dog

my_dog=Dog('Willie', 6)
your_dog=Dog('Rocky', 10)
print(f"\nMy dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.\n")
print(f"your dog's name is {your_dog.name}, and he is {your_dog.age} old.\n")

#Calling a method of the class Do

my_dog.sit()
my_dog.roll_over()
print("")
your_dog.sit()
your_dog.roll_over()