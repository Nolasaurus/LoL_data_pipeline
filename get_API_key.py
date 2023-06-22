def get_API_key():
    
    file_path = "API-key.txt" 

    try:
        with open(file_path, 'r') as file:
            API_key = file.read()
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

    return API_key