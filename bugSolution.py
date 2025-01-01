def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            file_content = f.read()
            print(file_content)
            # File automatically closed here
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

function_with_closed_file("some_file.txt")
