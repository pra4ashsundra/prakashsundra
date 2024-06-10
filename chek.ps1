import os

# Define the path to the directory
directory_path = r"C:\Prakash Jyotisa\Varshapala\periods"

# Check if the directory exists
if os.path.exists(directory_path):
    # Get the list of filenames
    filenames = os.listdir(directory_path)

    # Output the filenames
    for filename in filenames:
        print(filename)
else:
    print(f"The directory '{directory_path}' does not exist.")
