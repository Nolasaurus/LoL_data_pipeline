def get_API_key(file_path="API-key.txt"):
    API_key = None

    try:
        with open(file_path, 'r') as file:
            API_key = file.read().strip()  # strip() to remove any leading/trailing whitespace
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError:
        raise IOError(f"There was an error reading the file {file_path}.")

    if API_key:
        return API_key
    else:
        raise ValueError("API Key is empty.")
