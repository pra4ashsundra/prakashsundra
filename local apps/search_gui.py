import os
import fnmatch
import tkinter as tk
from tkinter import Listbox, Scrollbar
import subprocess

def search_files(drive, pattern):
    """Search for files matching the pattern in the specified drive."""
    matches = []
    for root, dirnames, filenames in os.walk(drive):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

def on_enter(event):
    pattern = entry.get()
    if not pattern:
        result.delete(0, tk.END)
        result.insert(tk.END, "Please enter a search pattern.")
        return

    result.delete(0, tk.END)  # Clear previous results
    matches = search_files('G:\\', pattern)
    
    if matches:
        for match in matches:
            result.insert(tk.END, match)
    else:
        result.insert(tk.END, "No files found.")

def open_folder(event):
    """Open the folder containing the selected file."""
    try:
        selected_file = result.get(result.curselection())
        folder_path = os.path.dirname(selected_file)
        subprocess.Popen(f'explorer /select,"{selected_file}"')
    except Exception as e:
        pass  # Ignore if there's an error

# Create the main window
root = tk.Tk()
root.title("File Search")

# Create and place the search entry
entry_label = tk.Label(root, text="Enter search pattern (e.g., *.txt) and press Enter:")
entry_label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Bind Enter key to search
entry.bind('<Return>', on_enter)

# Create a listbox to display results
result = Listbox(root, width=80, height=20)
result.pack(padx=10, pady=5)

# Add a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result.yview)

# Bind single-click event to open folder
result.bind('<ButtonRelease-1>', open_folder)

# Start the main loop
root.mainloop()
