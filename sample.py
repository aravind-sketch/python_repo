def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            
            # ✅ NEW: count occurrences of the word "data"
            count = data.lower().count("data")  # case-insensitive count
            
            if count > 0:
                print(m"Required word found {count} time(s)! [Feature branch change]")
                print(data)
            else:
                print("Word 'data' not found in file.")

    except FileNotFoundError:
        print("File not found!")

# Call the function
read_file("sample.txt")