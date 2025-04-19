# Create and write to input.txt
with open("input.txt", "w") as file:
    file.write("Hello, welcome to Python programming.\n")
    file.write("File handling is an important concept.\n")
    file.write("This script will process text data.\n")
    file.write("Counting words and converting text.\n")
    file.write("Writing results to another file.\n")

# Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()


# Convert text to uppercase
uppercase_content = content.upper()

# Write processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write(uppercase_content + "\n")

print("File modification complete! 'output.txt' has been created.")
try:
    filename = input("Enter the filename to read: ")
    with open(filename, "r") as file:
        content = file.read()
    print("File content successfully read!")
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied. Cannot read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
