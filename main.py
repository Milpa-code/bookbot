def get_book_text():
    with open("/home/milpa/git/bookbot/books/frankenstein.txt") as f:
        return f
def main():
    file_contents = []
    file_contents = f.read(get_book_text)
    return file_contents
print(main)