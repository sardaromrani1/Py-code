# A tkinter app that reads an Excel file using the 'pandas' library.

import tkinter as tk
from tkinter import filedialog
import pandas as pd

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx; *.xls")])

    if filename:
        df = pd.read_excel(filename)
        print(df)   # Just printing the DataFrame for demonstration


# Create the applicatoion window
root = tk.Tk()
root.title("Excel Reader")

# Create a button to browse for the Excel file
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

# Run the application
root.mainloop()