""" AUTHOR  - PRINCE SHARMA
    DATE    - 28/4/2024 10:22 PM
    WORKING - REPORTING
"""

import os

def read_file() :
    filename = input("Enter file name you want to read - ")
    try :
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError :
        print("File not found.")

def write_to_file() :
    filename = input("Enter file name you want to write - ")
    content = input("Enter what you want to write - ")
    with open(filename, 'w') as file :
        file.write(content)
        print(f"Content has been written to {filename}.")

def append_to_file() :
    filename = input("Enter file name you want to append - ")
    content = input("Enter what you want to append - ")
    with open(filename, 'a') as file :
        file.write(content)
        print(f"Content has been appended to {filename}.")

def create_file() :
    filename = input("Enter file name you want to create - ")
    content = input("Enter what you want to write - ")
    try :
        with open(filename, 'x') as file :
            file.write(content)
            print(f"File {filename} has been created.")
    except FileExistsError :
        print("File allready exists.")

def delete_file():
    filename = input("Enter file name you want to delete  - ")
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)

while True :
    print("1. read file")
    print("2. write file")
    print("3. append file")
    print("4. create file")
    print("5. delete file")
    print("6. exit")
    try :
        choice = int(input("Enter your choice - "))
        
        if choice == 1 :
            read_file()
        elif choice == 2 :
            write_to_file()
        elif choice == 3 :
            append_to_file()
        elif choice == 4 :
            create_file()
        elif choice == 5 :
            delete_file()
        else :
            break
    except :
        continue