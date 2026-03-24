# Simple program to read a file and print its contents

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            print("File Content:")
            print(data)
    except FileNotFoundError:
        print("File not found!")

# Call the function
read_file("sample.txt")