import sys
from stats import num_of_words, get_chars_dict, sort_dict

def main():
    # Check if the user provided the file path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error

    path = sys.argv[1]  # The first argument after the script name

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    try:
        with open(path, "r", encoding="utf-8") as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find the file '{path}'")
        sys.exit(1)

    word_count = num_of_words(file_contents)
    char_dict = get_chars_dict(file_contents)
    sorted_chars = sort_dict(char_dict)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
