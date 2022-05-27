import requests
file_path = 'C:/Users/jeroc/OneDrive/Desktop/Teanm Post Track.txt'

# if the file is in the same folder os the program use the following syntax
# file_name = 'pi_digits.txt'

with open(file_path) as file_object:

    # want to print the content of the file
#    contents = file_object.read()
# print(contents.rstrip())

  # want to print a list of lines form a file
    lines = file_object.read()
for line in lines:
    print(line.rstrip())