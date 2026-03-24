def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            
            if "data" in data:
                print("Required word found!")
                print(data)
            else:
                print("Word 'data' not found in file.")

    except FileNotFoundError:
        print("File not found!")

read_file("sample.txt")