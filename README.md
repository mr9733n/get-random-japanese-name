# Japanese Name Generator

This Python script generates random Japanese names by scraping data from [namegen.jp](https://namegen.jp/en). It allows you to specify the number of names to generate, gender, and whether to save the names to a file. The generated names are also logged for reference.

## Requirements

- Python 3.x
- Requests library (install using `pip install requests`)
- BeautifulSoup library (install using `pip install beautifulsoup4`)
- Unidecode library (install using `pip install unidecode`)

## Usage

1. Clone or download this repository.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script with the desired options. For example:

   ```bash
   python japanese_name_generator.py --num_names 5 --sex male --save_to_file
    ```

--num_names: Number of names to generate (default is 1).
--sex: Gender of names ('male' or 'female', default is 'male').
--save_to_file: Save generated names to a file (optional).

The script will generate random Japanese names based on your options and display them in the console.

If you chose to save the names to a file, you can find the file in the "output" directory.

## Logging

The script also logs its activities to a log file, which can be found in the "logs" directory. This log includes information about the requests made and the names generated.

