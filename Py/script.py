import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser

def open_url():
    url = address_entry.get()
    if url:
        webbrowser.open_new_tab(url)

def search():
    query = address_entry.get()
    if query:
        webbrowser.open_new_tab("https://www.google.com/search?q=" + query)

# Create the main application window
root = tk.Tk()
root.title("Simple Web Browser")

# Address Bar
address_frame = ttk.Frame(root)
address_frame.pack(fill=tk.X)

address_label = ttk.Label(address_frame, text="Enter URL:")
address_label.pack(side=tk.LEFT, padx=(5, 0), pady=5)

address_entry = ttk.Entry(address_frame)
address_entry.pack(fill=tk.X, padx=5, pady=5, expand=True)

go_button = ttk.Button(address_frame, text="Go", command=open_url)
go_button.pack(side=tk.RIGHT, padx=(0, 5), pady=5)

# Search Button
search_button = ttk.Button(root, text="Search", command=search)
search_button.pack(pady=5)

# Run the main event loop
root.mainloop()
