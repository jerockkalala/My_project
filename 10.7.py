# Assignment 10.1
# Jerock Kalala
# CIS-245 Introduction to Programming
# This program uses the OS library in order to validate that a directory exists before creating a file in that directory
# The program prompt the user for the directory they would like to save the file in as well as the name of the file.
# then prompt the program prompts the user for their name, address, and phone number. The program
# will write this data to a comma separated line in a file and store the file in the directory specified by the user.
# Once the data has been written the  program should read the file you just wrote to the file system and display
# the file contents to the user for validation purposes.

import os

# create the main function


def main():

    # Prompt the user for inputs
    directory = input("Please enter the path of the directory you want to store your file : ")
    file_name = input("now enter the name of the file you want to create: ")
    name = input("Enter a name you want to store in the file : ")
    address = input("Enter the address : ")
    phone_number = input("Finally, the phone number you want to store in the file: ")

# Input validation: check if the directory exists
    if os.path.isdir(directory):

        # Create and open the file to write
        file = open(os.path.join(directory, file_name), 'w')

        # write the data by comma separated
        file.write(name+',' + address + ',' + phone_number+'\n')
        file.close()  # close the file after writing is done
        print("Here is the content of the created file: \n")  # Output the file

        # Read the file
        read_file = open(os.path.join(directory, file_name), 'r')
        for line in read_file:
            print(line)
        read_file.close()  # closing the file object
    else:
        print("Sorry that directory is not exists...")

# Create a print function


def message():
    print("information successfully saved.")
    print("Thank you for using this program.")

# calling function


main()
answer = input(print("Double check the above information if they are correct? Press 'Y' to save or press 'N' for No: "))
if answer == 'y':
    message()
else:
    main()
