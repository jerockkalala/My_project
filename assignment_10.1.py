import os.path

# Prompt the user to enter the directory name
directory = input("Please enter the path of the directory you want to store your file : ")

# Prompt the user to enter the file name
file_name = input("now enter the name of the file you want to create: ")

# validate if the directory exist or not
if not os.path.isdir(directory):
    os.makedirs(directory)   # if not exist, we make the same

# creating the full path with the file name
path = directory + file_name

# file object to open the file
# if file already exist (used 'e') it opens otherwise creates a new
file_name1 = open(path, 'a')

# Ask the user to enter: the name, the address and the phone to be written in the file
name = input("Enter a name you want to store in the file : ")
file_name1.write(name + ',')  # writing the name with a comma
address = input("Enter the address you want to store in the file: ")
file_name1.write(address + ',') # writing the address with a comma
phone = input("Enter the phone number you want to store in the file: ")
file_name1.write(phone) # writing the phone number with a comma

# closing the file object
file_name1.close()

#  Output the created file
file_name2 = open(path, 'r')
result = file_name2.readlines()
print("\nHere is the data from the created file : \n", result)
file_name2.close()
