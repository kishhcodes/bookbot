import sys

from stats import get_words_count, sort_it

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    book_text = get_book_text(book_file)
    word_count = get_words_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_characters = sort_it(book_text)
    for i in range(0, len(sorted_characters)):
        print(f"{sorted_characters[i]['char']}: {sorted_characters[i]['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
