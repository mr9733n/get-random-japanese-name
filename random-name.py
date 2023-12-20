import json
import random
import argparse

# Load data from a JSON file
def load_data(json_filename):
    with open(json_filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

# Get a random entry
def get_random_entry(data, entry_type):
    if entry_type not in data:
        return "Invalid entry type"
    return random.choice(data[entry_type])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random entries from a JSON file")
    parser.add_argument('--json', type=str, default='names.json', help='Path to the JSON file with data')
    parser.add_argument('--entry_types', nargs='+', default=['full_name', 'first_name', 'last_name'], help='Entry types for generation')

    args = parser.parse_args()

    data = load_data(args.json)

    # Usage examples
    for entry_type in args.entry_types:
        random_entry = get_random_entry(data, entry_type)
        print(f"Random {entry_type.replace('_', ' ')}: {random_entry}")
