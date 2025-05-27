def get_book_text():
    with open("books/frankenstein.txt", 'w', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)