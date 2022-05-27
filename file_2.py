import requests
# file_path = 'C:/Users/jeroc/OneDrive/Desktop/Teanm Post Track.txt'

# if the file is in the same folder os the program use the following syntax
file_name = 'pi_digits.txt'

# If we want to read line by line
with open(file_name) as file_object:
#    for line in file_object:
#        print(line.strip())

  # want to print a list of lines form a file
    lines = file_object.read()
for line in lines:
    print(line.rstrip())