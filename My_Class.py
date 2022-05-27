class User:
    def __init__(self, fname, lname, color, age):
        self.fname = fname
        self.lname = lname
        self.color = color
        self.age = age
    def describe_user(self):
        print(f"{self.fname} {self.lname} is {self.color} color, and is {self.age} year(s) old.")

    def greet_user(self):
        print(f"Hello {self.fname} {self.lname}!")

#create instances
person_1 = User('Elvis', 'Kabasele', 'Black', 41)
person_2 = User('Maria', 'Tshilemba', 'White', 39)
person_3 = User('Jerock', 'Kalala', 'Black', 37)

person_1.describe_user()
person_2.describe_user()
person_3.describe_user()
print("")
person_1.greet_user()
person_2.greet_user()
person_3.greet_user()