import tkinter as tk
from tkinter import ttk
import json
import random
import pyperclip

def load_data(json_filename):
    with open(json_filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def get_random_entry(data, entry_type):
    if entry_type not in data:
        return "Invalid entry type"
    return random.choice(data[entry_type])

def generate_random_entry():
    selected_entry_type = entry_type_combobox.get()
    random_entry = get_random_entry(data, selected_entry_type)
    result_label.config(text=f"Random {selected_entry_type.replace('_', ' ')}: {random_entry}")
    
    pyperclip.copy(random_entry)

root = tk.Tk()
root.title("Random Entry Generator")
root.geometry("300x150")  

data = load_data('names.json')

entry_type_label = ttk.Label(root, text="Select Entry Type:")
entry_type_label.pack(pady=10)  

entry_types = ['full_name', 'first_name', 'last_name']
entry_type_combobox = ttk.Combobox(root, values=entry_types)
entry_type_combobox.pack(pady=5) 
entry_type_combobox.set(entry_types[0])

generate_button = ttk.Button(root, text="Generate", command=generate_random_entry)
generate_button.pack(pady=10)  

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
