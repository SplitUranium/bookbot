from stats import word_count, char_count, sort_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = (get_book_text(book_path))
    num_words = word_count(text)
    characters = char_count(text)
    sorted_list = sort_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    contents = ""
    with open(filepath) as file:
        contents = file.read()
    return contents


main()
