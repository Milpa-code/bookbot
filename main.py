def get_book_text(filepath):
    with open(filepath) as f:
        read_text = f.read()
    return read_text
def main():
    result = get_book_text("books/frankenstein.txt")
    print(result)
from stats import word_count