import argparse
from japanese_name_generator import JapaneseNameGenerator

def main():
    parser = argparse.ArgumentParser(description="Generate random Japanese names.")
    parser.add_argument("--num_names", type=int, default=1, help="Number of names to generate")
    parser.add_argument("--save_to_file", action="store_true", help="Save names to a file")
    parser.add_argument("--sex", type=str, default="male", help="Gender (e.g., 'male', 'female')")
    parser.add_argument("--log_to_file", action="store_true", help="Save log to a file") 

    args = parser.parse_args()

    name_generator = JapaneseNameGenerator(
        num_names=args.num_names,
        save_to_file=args.save_to_file,
        params={"sex": args.sex},
        log_to_file=args.log_to_file 
    )

    random_names = name_generator.generate_names()
    if random_names:
        print("Behold your results!")
        for i, name in enumerate(random_names, 1):
            print(name)

if __name__ == "__main__":
    main()
