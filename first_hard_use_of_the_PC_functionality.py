import winreg
import os
import tkinter as tk
from datetime import datetime


# Function to get the first use of the PC
def get_first_pc_use():
    # Specify the path to the Registry hive file
    registry_file_path = r"C:/Windows/System32/config/SOFTWARE"

    if os.path.exists(registry_file_path):
        # Get the creation timestamp of the file
        creation_timestamp = os.path.getctime(registry_file_path)
        # Convert the timestamp to a readable datetime object
        first_use_datetime = datetime.fromtimestamp(creation_timestamp)
        return first_use_datetime
    else:
        return None


# Create a Tkinter window
window = tk.Tk()
window.geometry ("300x100+150+150")

# Add a label to display the first use of the PC
first_use_label = tk.Label(window, text="First PC Use: ")
first_use_label.pack()


# Function to update the label text with the first use of the PC
def update_first_use_label():
    first_use_datetime = get_first_pc_use()
    if first_use_datetime:
        first_use_label["text"] = "The First Time Your pc was used is : \n" + str(first_use_datetime)
    else:
        first_use_label["text"] = " After Searching We couldn't find it, SORRY :("


# Button to update the first use label
update_button = tk.Button(window, text="SEARCH", command=update_first_use_label)
update_button.pack()

# Run the Tkinter event loop
window.mainloop()
