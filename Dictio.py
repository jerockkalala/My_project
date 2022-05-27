# Creates key, value for dict based on user input
# Combine with loops to avoid manual repetition

class_list = dict()
print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
key = input("Enter key: ")
value = input("Enter value: ")
class_list[key] = [value]
print(f"{class_list}")