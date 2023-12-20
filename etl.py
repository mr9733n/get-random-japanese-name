import os
import json

# Create lists for names
full_name = []
first_name = []
last_name = []

# List of paths to folders with txt files
folder_paths = [
    'F:\\9834758345hf7A\\get-random-jp-name\\output',
    'F:\\9834758345hf7A\\get-random-jp-name\\dist\\output',
    'F:\\9834758345hf7A\\get-random-jp-name\\flask\\output',
    'F:\9834758345hf7A\get-random-japanese-name\flask\output'
    # Add more folder paths here if needed
]

# Iterate over each folder path
for folder_path in folder_paths:
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                lines = file.readlines()
                # Add each name from each line to the respective list
                for line in lines:
                    name = line.strip()
                    if name:
                        full_name.append(name)
                        name_parts = name.split()
                        if len(name_parts) >= 2:
                            first_name.append(name_parts[0])
                            last_name.append(name_parts[-1])

# Save lists in JSON format
with open('names.json', 'w', encoding='utf-8') as json_file:
    data = {
        'full_name': full_name,
        'first_name': first_name,
        'last_name': last_name
    }
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Data successfully processed and saved in the names.json file")
